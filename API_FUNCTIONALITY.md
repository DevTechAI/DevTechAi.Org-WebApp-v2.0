# Express API Functionality Overview

## Current Status
The Express API server is currently a **basic skeleton** with controllers defined but **not yet connected to routes**. The server only has 2 basic endpoints active.

## Currently Active Endpoints

### 1. Health Check
- **GET** `/health`
- Returns server status and version information
- Response:
  ```json
  {
    "status": "ok",
    "timestamp": "2025-11-09T...",
    "service": "DevTechAI WebApp v2.0 API",
    "version": "2.0.0"
  }
  ```

### 2. API Info
- **GET** `/api`
- Returns API information and available endpoints
- Response:
  ```json
  {
    "message": "DevTechAI WebApp v2.0 API",
    "version": "2.0.0",
    "endpoints": {
      "health": "/health",
      "api": "/api"
    }
  }
  ```

## Available Controllers (Not Yet Connected)

The following controllers are implemented but **not yet wired up to routes** in `server.ts`:

### 1. AuthController
**Authentication & Authorization**

- `login(req, res, next)` - User login with email/password
- `register(req, res, next)` - User registration
- `refreshToken(req, res, next)` - Refresh access token
- `logout(req, res, next)` - User logout

**Features:**
- JWT token generation
- Password hashing with bcrypt
- Support for Auth0, Firebase Auth, and custom JWT
- Token refresh mechanism

### 2. UserController
**User Management**

- `getUsers(req, res, next)` - List users with pagination, search, and filtering
- `getUserById(req, res, next)` - Get user by ID
- `updateUser(req, res, next)` - Update user information
- `deleteUser(req, res, next)` - Delete user

**Features:**
- Pagination support
- Search by email/name
- Filter by role
- User CRUD operations

### 3. AIController
**AI/LLM Integration**

- `chat(req, res, next)` - AI chat completion
- `generateImage(req, res, next)` - AI image generation
- `getModels(req, res, next)` - List available AI models

**Features:**
- Multi-model support (OpenAI, Anthropic, Google AI, Azure AI)
- Chat completions
- Image generation (DALL-E, etc.)
- Model information

### 4. WorkflowController
**Workflow Automation**

- `getWorkflows(req, res, next)` - List workflows with filtering
- `createWorkflow(req, res, next)` - Create new workflow
- `executeWorkflow(req, res, next)` - Execute a workflow

**Features:**
- N8N integration support
- Workflow CRUD operations
- Workflow execution
- Status and category filtering

### 5. MonitoringController
**System Monitoring**

- `healthCheck(req, res, next)` - Comprehensive health check
- `getMetrics(req, res, next)` - System and application metrics

**Features:**
- Database health check
- Redis health check
- System metrics (CPU, memory, uptime)
- Application metrics (requests, response time, errors)
- Datadog integration support

## Middleware

The server includes:
- **Helmet** - Security headers
- **CORS** - Cross-origin resource sharing
- **Compression** - Response compression
- **JSON parsing** - Request body parsing
- **Error handling** - Centralized error handling
- **404 handler** - Not found route handler

## To Connect Controllers to Routes

Currently, the controllers are commented out in `server.ts`. To activate them, you would need to:

1. Uncomment the import: `import { AuthController, UserController, AIController, WorkflowController, MonitoringController } from './api/controllers';`

2. Create route handlers, for example:
   ```typescript
   const authController = new AuthController();
   app.post('/api/auth/login', authController.login.bind(authController));
   app.post('/api/auth/register', authController.register.bind(authController));
   // ... etc
   ```

## Database Integration

The controllers are designed to work with:
- **Supabase** (PostgreSQL)
- **PostgreSQL** (direct)
- **Firebase Firestore** (commented out - requires package)
- **MongoDB** (commented out - requires package)

## Service Integrations

- **AI Services**: OpenAI, Anthropic, Google AI, Azure AI
- **Workflow**: N8N
- **Monitoring**: Datadog
- **Auth**: Auth0, Firebase Auth, Custom JWT

## Summary

**Current State:**
- ✅ Basic server running on port 3001
- ✅ Health check endpoint active
- ✅ Controllers implemented but not connected
- ⚠️ Most functionality exists but needs route wiring

**To Use Full Functionality:**
- Connect controllers to routes in `server.ts`
- Set up environment variables for services
- Configure database connections
- Install optional packages if needed (firebase, mongodb, auth0, @azure/openai)

