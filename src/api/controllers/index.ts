// API Route Handlers
import { Request, Response, NextFunction } from 'express';
import bcrypt from 'bcryptjs';
import { AuthServiceFactory } from '../../services/auth/auth0';
import { DatabaseServiceFactory } from '../../services/database/supabase';
import { AIServiceFactory } from '../../services/ai/openai';
import { WorkflowServiceFactory } from '../../services/workflow/n8n';
import { MonitoringServiceFactory } from '../../services/monitoring/datadog';

// Authentication Routes
export class AuthController {
  private authService: any;
  private dbService: any;

  constructor() {
    this.authService = AuthServiceFactory.createService(
      process.env.AUTH_PROVIDER || 'jwt',
      {
        secret: process.env.JWT_SECRET,
        expiresIn: process.env.JWT_EXPIRES_IN || '15m',
        refreshExpiresIn: process.env.JWT_REFRESH_EXPIRES_IN || '7d'
      }
    );
    
    this.dbService = DatabaseServiceFactory.createService(
      process.env.DATABASE_PROVIDER || 'postgresql',
      {
        host: process.env.DATABASE_HOST,
        port: parseInt(process.env.DATABASE_PORT || '5432'),
        database: process.env.DATABASE_NAME,
        user: process.env.DATABASE_USER,
        password: process.env.DATABASE_PASSWORD
      }
    );
  }

  async login(req: Request, res: Response, next: NextFunction) {
    try {
      const { email, password } = req.body;

      if (!email || !password) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Email and password are required'
          }
        });
      }

      const result = await this.authService.authenticate({ email, password });

      res.json({
        success: true,
        data: result
      });
    } catch (error) {
      next(error);
    }
  }

  async register(req: Request, res: Response, next: NextFunction) {
    try {
      const { email, password, name } = req.body;

      if (!email || !password || !name) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Email, password, and name are required'
          }
        });
      }

      // Check if user already exists
      const existingUser = await this.dbService.query(
        'SELECT id FROM users WHERE email = $1',
        [email]
      );

      if (existingUser.length > 0) {
        return res.status(409).json({
          success: false,
          error: {
            code: 'USER_EXISTS',
            message: 'User with this email already exists'
          }
        });
      }

      // Create user
      const hashedPassword = await bcrypt.hash(password, 10);
      const user = await this.dbService.query(
        'INSERT INTO users (email, password, name) VALUES ($1, $2, $3) RETURNING id, email, name, created_at',
        [email, hashedPassword, name]
      );

      // Generate tokens
      const result = await this.authService.authenticate({ email, password });

      res.status(201).json({
        success: true,
        data: result
      });
    } catch (error) {
      next(error);
    }
  }

  async refreshToken(req: Request, res: Response, next: NextFunction) {
    try {
      const { refreshToken } = req.body;

      if (!refreshToken) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Refresh token is required'
          }
        });
      }

      const result = await this.authService.refreshToken(refreshToken);

      res.json({
        success: true,
        data: result
      });
    } catch (error) {
      next(error);
    }
  }

  async logout(req: Request, res: Response, next: NextFunction) {
    try {
      const token = req.headers.authorization?.replace('Bearer ', '');

      if (!token) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Token is required'
          }
        });
      }

      await this.authService.logout(token);

      res.json({
        success: true,
        data: { message: 'Logged out successfully' }
      });
    } catch (error) {
      next(error);
    }
  }
}

// User Management Routes
export class UserController {
  private dbService: any;

  constructor() {
    this.dbService = DatabaseServiceFactory.createService(
      process.env.DATABASE_PROVIDER || 'postgresql',
      {
        host: process.env.DATABASE_HOST,
        port: parseInt(process.env.DATABASE_PORT || '5432'),
        database: process.env.DATABASE_NAME,
        user: process.env.DATABASE_USER,
        password: process.env.DATABASE_PASSWORD
      }
    );
  }

  async getUsers(req: Request, res: Response, next: NextFunction) {
    try {
      const { page = 1, limit = 20, search, role } = req.query;
      const offset = (Number(page) - 1) * Number(limit);

      let query = 'SELECT id, email, name, roles, created_at, last_login_at FROM users';
      const params: any[] = [];
      let paramCount = 0;

      const conditions: string[] = [];

      if (search) {
        paramCount++;
        conditions.push(`(email ILIKE $${paramCount} OR name ILIKE $${paramCount})`);
        params.push(`%${search}%`);
      }

      if (role) {
        paramCount++;
        conditions.push(`$${paramCount} = ANY(roles)`);
        params.push(role);
      }

      if (conditions.length > 0) {
        query += ' WHERE ' + conditions.join(' AND ');
      }

      query += ` ORDER BY created_at DESC LIMIT $${paramCount + 1} OFFSET $${paramCount + 2}`;
      params.push(Number(limit), offset);

      const users = await this.dbService.query(query, params);

      // Get total count
      let countQuery = 'SELECT COUNT(*) FROM users';
      if (conditions.length > 0) {
        countQuery += ' WHERE ' + conditions.join(' AND ');
      }
      const countResult = await this.dbService.query(countQuery, params.slice(0, -2));
      const total = parseInt(countResult[0].count);

      res.json({
        success: true,
        data: {
          users,
          pagination: {
            page: Number(page),
            limit: Number(limit),
            total,
            totalPages: Math.ceil(total / Number(limit))
          }
        }
      });
    } catch (error) {
      next(error);
    }
  }

  async getUserById(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;

      const users = await this.dbService.query(
        'SELECT id, email, name, roles, created_at, updated_at, last_login_at FROM users WHERE id = $1',
        [id]
      );

      if (users.length === 0) {
        return res.status(404).json({
          success: false,
          error: {
            code: 'RESOURCE_NOT_FOUND',
            message: 'User not found'
          }
        });
      }

      res.json({
        success: true,
        data: { user: users[0] }
      });
    } catch (error) {
      next(error);
    }
  }

  async updateUser(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;
      const { name, roles } = req.body;

      const updateFields: string[] = [];
      const params: any[] = [];
      let paramCount = 0;

      if (name !== undefined) {
        paramCount++;
        updateFields.push(`name = $${paramCount}`);
        params.push(name);
      }

      if (roles !== undefined) {
        paramCount++;
        updateFields.push(`roles = $${paramCount}`);
        params.push(roles);
      }

      if (updateFields.length === 0) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'No fields to update'
          }
        });
      }

      paramCount++;
      updateFields.push(`updated_at = NOW()`);
      params.push(id);

      const query = `UPDATE users SET ${updateFields.join(', ')} WHERE id = $${paramCount} RETURNING id, email, name, roles, created_at, updated_at`;

      const users = await this.dbService.query(query, params);

      if (users.length === 0) {
        return res.status(404).json({
          success: false,
          error: {
            code: 'RESOURCE_NOT_FOUND',
            message: 'User not found'
          }
        });
      }

      res.json({
        success: true,
        data: { user: users[0] }
      });
    } catch (error) {
      next(error);
    }
  }

  async deleteUser(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;

      const result = await this.dbService.query(
        'DELETE FROM users WHERE id = $1 RETURNING id',
        [id]
      );

      if (result.length === 0) {
        return res.status(404).json({
          success: false,
          error: {
            code: 'RESOURCE_NOT_FOUND',
            message: 'User not found'
          }
        });
      }

      res.json({
        success: true,
        data: { message: 'User deleted successfully' }
      });
    } catch (error) {
      next(error);
    }
  }
}

// AI Service Routes
export class AIController {
  private aiService: any;

  constructor() {
    this.aiService = AIServiceFactory.createService(
      process.env.AI_PROVIDER || 'openai',
      {
        apiKey: process.env.OPENAI_API_KEY
      }
    );
  }

  async chat(req: Request, res: Response, next: NextFunction) {
    try {
      const { message, model, context } = req.body;

      if (!message) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Message is required'
          }
        });
      }

      const messages = [
        { role: 'system', content: 'You are a helpful AI assistant.' },
        { role: 'user', content: message }
      ];

      const response = await this.aiService.chatCompletion(messages, {
        model: model || 'gpt-4',
        temperature: 0.7,
        maxTokens: 1000
      });

      res.json({
        success: true,
        data: {
          response: response.content,
          model: response.model,
          usage: response.usage,
          conversationId: context?.conversationId
        }
      });
    } catch (error) {
      next(error);
    }
  }

  async generateImage(req: Request, res: Response, next: NextFunction) {
    try {
      const { prompt, model, size, quality } = req.body;

      if (!prompt) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Prompt is required'
          }
        });
      }

      const response = await this.aiService.generateImage(prompt, {
        model: model || 'dall-e-3',
        size: size || '1024x1024',
        quality: quality || 'standard'
      });

      res.json({
        success: true,
        data: {
          images: response.images,
          model: response.model
        }
      });
    } catch (error) {
      next(error);
    }
  }

  async getModels(req: Request, res: Response, next: NextFunction) {
    try {
      const models = [
        { id: 'gpt-4', name: 'GPT-4', type: 'chat' },
        { id: 'gpt-3.5-turbo', name: 'GPT-3.5 Turbo', type: 'chat' },
        { id: 'dall-e-3', name: 'DALL-E 3', type: 'image' },
        { id: 'text-davinci-003', name: 'Text Davinci 003', type: 'text' }
      ];

      res.json({
        success: true,
        data: { models }
      });
    } catch (error) {
      next(error);
    }
  }
}

// Workflow Routes
export class WorkflowController {
  private workflowService: any;
  private dbService: any;

  constructor() {
    this.workflowService = WorkflowServiceFactory.createService(
      process.env.WORKFLOW_PROVIDER || 'n8n',
      {
        baseURL: process.env.N8N_BASE_URL,
        apiKey: process.env.N8N_API_KEY
      }
    );
    
    this.dbService = DatabaseServiceFactory.createService(
      process.env.DATABASE_PROVIDER || 'postgresql',
      {
        host: process.env.DATABASE_HOST,
        port: parseInt(process.env.DATABASE_PORT || '5432'),
        database: process.env.DATABASE_NAME,
        user: process.env.DATABASE_USER,
        password: process.env.DATABASE_PASSWORD
      }
    );
  }

  async getWorkflows(req: Request, res: Response, next: NextFunction) {
    try {
      const { status, category, userId } = req.query;

      let query = 'SELECT * FROM workflows WHERE 1=1';
      const params: any[] = [];
      let paramCount = 0;

      if (status) {
        paramCount++;
        query += ` AND status = $${paramCount}`;
        params.push(status);
      }

      if (category) {
        paramCount++;
        query += ` AND category = $${paramCount}`;
        params.push(category);
      }

      if (userId) {
        paramCount++;
        query += ` AND user_id = $${paramCount}`;
        params.push(userId);
      }

      query += ' ORDER BY created_at DESC';

      const workflows = await this.dbService.query(query, params);

      res.json({
        success: true,
        data: { workflows }
      });
    } catch (error) {
      next(error);
    }
  }

  async createWorkflow(req: Request, res: Response, next: NextFunction) {
    try {
      const { name, description, trigger, steps } = req.body;

      if (!name || !trigger || !steps) {
        return res.status(400).json({
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Name, trigger, and steps are required'
          }
        });
      }

      const workflow = await this.dbService.query(
        'INSERT INTO workflows (name, description, trigger, steps, user_id, status) VALUES ($1, $2, $3, $4, $5, $6) RETURNING *',
        [name, description, JSON.stringify(trigger), JSON.stringify(steps), (req as any).user?.id, 'draft']
      );

      res.status(201).json({
        success: true,
        data: { workflow: workflow[0] }
      });
    } catch (error) {
      next(error);
    }
  }

  async executeWorkflow(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;
      const { inputData } = req.body;

      const workflows = await this.dbService.query(
        'SELECT * FROM workflows WHERE id = $1',
        [id]
      );

      if (workflows.length === 0) {
        return res.status(404).json({
          success: false,
          error: {
            code: 'RESOURCE_NOT_FOUND',
            message: 'Workflow not found'
          }
        });
      }

      const workflow = workflows[0];

      if (workflow.status !== 'active') {
        return res.status(400).json({
          success: false,
          error: {
            code: 'WORKFLOW_INACTIVE',
            message: 'Workflow is not active'
          }
        });
      }

      const result = await this.workflowService.executeWorkflow(id, inputData);

      res.json({
        success: true,
        data: {
          executionId: result.id,
          status: result.status,
          result: result.data
        }
      });
    } catch (error) {
      next(error);
    }
  }
}

// Monitoring Routes
export class MonitoringController {
  private monitoringService: any;

  constructor() {
    this.monitoringService = MonitoringServiceFactory.createService(
      process.env.MONITORING_PROVIDER || 'datadog',
      {
        host: process.env.DATADOG_HOST,
        port: parseInt(process.env.DATADOG_PORT || '8125'),
        apiKey: process.env.DATADOG_API_KEY
      }
    );
  }

  async healthCheck(req: Request, res: Response, next: NextFunction) {
    try {
      const health = {
        status: 'healthy',
        timestamp: new Date().toISOString(),
        version: process.env.APP_VERSION || '1.0.0',
        uptime: process.uptime(),
        services: {}
      };

      // Check database
      try {
        const dbService = DatabaseServiceFactory.createService(
          process.env.DATABASE_PROVIDER || 'postgresql',
          {
            host: process.env.DATABASE_HOST,
            port: parseInt(process.env.DATABASE_PORT || '5432'),
            database: process.env.DATABASE_NAME,
            user: process.env.DATABASE_USER,
            password: process.env.DATABASE_PASSWORD
          }
        );
        await dbService.healthCheck();
        (health.services as any).database = 'healthy';
      } catch (error) {
        (health.services as any).database = 'unhealthy';
        health.status = 'unhealthy';
      }

      // Check Redis
      try {
        const redis = require('redis').createClient({
          url: process.env.REDIS_URL
        });
        await redis.ping();
        (health.services as any).redis = 'healthy';
      } catch (error) {
        (health.services as any).redis = 'unhealthy';
        health.status = 'unhealthy';
      }

      const statusCode = health.status === 'healthy' ? 200 : 503;
      res.status(statusCode).json({
        success: true,
        data: health
      });
    } catch (error) {
      next(error);
    }
  }

  async getMetrics(req: Request, res: Response, next: NextFunction) {
    try {
      const metrics = {
        timestamp: new Date().toISOString(),
        system: {
          cpu: process.cpuUsage(),
          memory: process.memoryUsage(),
          uptime: process.uptime()
        },
        application: {
          requests: await this.monitoringService.getMetric('http_requests_total'),
          responseTime: await this.monitoringService.getMetric('http_request_duration_seconds'),
          errors: await this.monitoringService.getMetric('http_requests_total', { status_code: '5..' })
        }
      };

      res.json({
        success: true,
        data: metrics
      });
    } catch (error) {
      next(error);
    }
  }
}
