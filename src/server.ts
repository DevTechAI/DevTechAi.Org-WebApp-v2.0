/**
 * DevTechAI WebApp v2.0 - Express Server
 * Main server entry point for the backend API
 */

import express, { Express, Request, Response, NextFunction } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import compression from 'compression';
import dotenv from 'dotenv';
import { createServer } from 'http';
import path from 'path';
import multer from 'multer';

// Load environment variables
dotenv.config();

// Import Supabase client directly
import { createClient } from '@supabase/supabase-js';

// Import routes and middleware
// import { AuthController } from './api/controllers';

const app: Express = express();
const PORT = 8001; // Use a fixed port to avoid conflicts
const upload = multer();

// Initialize Supabase client directly
const supabase = createClient(
  process.env.SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY! // Use service role key for server-side operations
);

console.log('✅ Supabase client initialized');

// Middleware
app.use(helmet());
app.use(cors({
  origin: true, // Allow all origins (simpler for dev environments)
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  credentials: true
}));
app.use(compression());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from public directory
app.use(express.static(path.join(process.cwd(), 'public')));

// Serve static files from root directory (for index.html)
app.use(express.static(process.cwd()));

// Health check endpoint
app.get('/health', (req: Request, res: Response) => {
  res.status(200).json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    service: 'DevTechAI WebApp v2.0 API',
    version: '2.0.0'
  });
});

// Serve the main website
app.get('/', (req: Request, res: Response) => {
  res.sendFile(path.join(process.cwd(), 'index.html'));
});

// API routes
app.get('/api', (req: Request, res: Response) => {
  res.json({
    message: 'DevTechAI WebApp v2.0 API',
    version: '2.0.0',
    endpoints: {
      health: '/health',
      api: '/api',
      contact: '/api/contact'
    }
  });
});

// Contact form submission endpoint
app.post('/api/contact', upload.none(), async (req: Request, res: Response) => {
  try {
    console.log('📨 Contact form submission received:');
    console.log('Headers:', req.headers);
    console.log('Body:', req.body);
    console.log('Content-Type:', req.get('content-type'));

    const { name, email, subject, message } = req.body;

    // Validation
    if (!name || !email || !subject || !message) {
      console.log('❌ Validation failed - missing fields:', { name: !!name, email: !!email, subject: !!subject, message: !!message });
      return res.status(400).json({
        error: 'Validation Error',
        message: 'All fields are required: name, email, subject, message'
      });
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      console.log('❌ Invalid email format:', email);
      return res.status(400).json({
        error: 'Validation Error',
        message: 'Invalid email format'
      });
    }

    // Insert contact into Supabase
    const contactData = {
      name: name.trim(),
      email: email.trim().toLowerCase(),
      subject: subject.trim(),
      message: message.trim()
    };

    console.log('💾 Attempting to save to Supabase:', contactData);

    const { data: result, error } = await supabase
      .from('contacts')
      .insert(contactData)
      .select()
      .single();

    if (error) {
      console.log('❌ Supabase error:', error);
      throw error;
    }

    console.log('✅ New contact submitted:', result.id);

    res.status(200).json({
      success: true,
      message: `Message received, ${name}. Our experts will reach out shortly.`,
      contactId: result.id
    });

  } catch (error: any) {
    console.error('❌ Contact form error:');
    console.error('Error details:', error);
    console.error('Error message:', error.message);
    console.error('Error code:', error.code);

    res.status(500).json({
      error: 'Server Error',
      message: 'Failed to submit contact form. Please try again later.',
      details: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
});

// Error handling middleware
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Error:', err);
  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Something went wrong'
  });
});

// 404 handler
app.use((req: Request, res: Response) => {
  res.status(404).json({
    error: 'Not Found',
    message: `Route ${req.path} not found`
  });
});

// Create HTTP server
const server = createServer(app);

// Start server
server.listen(PORT, () => {
  console.log(`🚀 DevTechAI API Server running on port ${PORT}`);
  console.log(`📡 Health check: http://localhost:${PORT}/health`);
  console.log(`🔗 API endpoint: http://localhost:${PORT}/api`);
  console.log(`🌍 Environment: ${process.env.NODE_ENV || 'development'}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  server.close(() => {
    console.log('HTTP server closed');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT signal received: closing HTTP server');
  server.close(() => {
    console.log('HTTP server closed');
    process.exit(0);
  });
});

export default app;

// Restart trigger
