# API Documentation

## Overview

The DevTechAI WebApp v2.0 provides a comprehensive REST API for all application functionality. This document describes all available endpoints, request/response formats, and authentication requirements.

## Base URL

- **Development**: `http://localhost:3000/api`
- **Staging**: `https://staging-api.devtechai.org/api`
- **Production**: `https://api.devtechai.org/api`

## Authentication

All API endpoints require authentication unless explicitly marked as public. The API supports multiple authentication methods:

### JWT Token Authentication
```http
Authorization: Bearer <jwt_token>
```

### API Key Authentication
```http
X-API-Key: <api_key>
```

### OAuth2/OIDC
```http
Authorization: Bearer <oauth_token>
```

## Response Format

All API responses follow a consistent format:

### Success Response
```json
{
  "success": true,
  "data": {
    // Response data
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "requestId": "req_123456789"
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {
      // Additional error details
    }
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "requestId": "req_123456789"
  }
}
```

## API Endpoints

### Authentication Endpoints

#### POST /auth/login
Authenticate user and return JWT token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "token": "jwt_token_here",
    "refreshToken": "refresh_token_here",
    "user": {
      "id": "user_123",
      "email": "user@example.com",
      "name": "John Doe",
      "roles": ["user"]
    }
  }
}
```

#### POST /auth/register
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe"
}
```

#### POST /auth/refresh
Refresh JWT token using refresh token.

**Request Body:**
```json
{
  "refreshToken": "refresh_token_here"
}
```

#### POST /auth/logout
Logout user and invalidate tokens.

### User Management Endpoints

#### GET /users
Get list of users (admin only).

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20)
- `search`: Search term
- `role`: Filter by role

**Response:**
```json
{
  "success": true,
  "data": {
    "users": [
      {
        "id": "user_123",
        "email": "user@example.com",
        "name": "John Doe",
        "roles": ["user"],
        "createdAt": "2024-01-01T00:00:00Z",
        "lastLogin": "2024-01-01T00:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 100,
      "totalPages": 5
    }
  }
}
```

#### GET /users/:id
Get user by ID.

#### PUT /users/:id
Update user information.

#### DELETE /users/:id
Delete user account (admin only).

### AI Service Endpoints

#### POST /ai/chat
Send message to AI chat service.

**Request Body:**
```json
{
  "message": "Hello, how can you help me?",
  "model": "gpt-4",
  "context": {
    "conversationId": "conv_123",
    "userId": "user_123"
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "response": "I can help you with various tasks...",
    "model": "gpt-4",
    "usage": {
      "promptTokens": 20,
      "completionTokens": 50,
      "totalTokens": 70
    },
    "conversationId": "conv_123"
  }
}
```

#### POST /ai/generate-image
Generate image using AI.

**Request Body:**
```json
{
  "prompt": "A beautiful sunset over mountains",
  "model": "dall-e-3",
  "size": "1024x1024",
  "quality": "standard"
}
```

#### GET /ai/models
Get available AI models.

### Workflow Endpoints

#### GET /workflows
Get list of workflows.

**Query Parameters:**
- `status`: Filter by status (active, inactive, draft)
- `category`: Filter by category
- `userId`: Filter by user

#### POST /workflows
Create new workflow.

**Request Body:**
```json
{
  "name": "Email Notification Workflow",
  "description": "Send email when user registers",
  "trigger": {
    "type": "webhook",
    "config": {
      "url": "/webhooks/user-registered"
    }
  },
  "steps": [
    {
      "type": "email",
      "config": {
        "template": "welcome-email",
        "recipient": "{{user.email}}"
      }
    }
  ]
}
```

#### GET /workflows/:id
Get workflow by ID.

#### PUT /workflows/:id
Update workflow.

#### POST /workflows/:id/execute
Execute workflow manually.

#### DELETE /workflows/:id
Delete workflow.

### Monitoring Endpoints

#### GET /monitoring/health
Health check endpoint.

**Response:**
```json
{
  "success": true,
  "data": {
    "status": "healthy",
    "timestamp": "2024-01-01T00:00:00Z",
    "services": {
      "database": "healthy",
      "redis": "healthy",
      "external-apis": "healthy"
    }
  }
}
```

#### GET /monitoring/metrics
Get application metrics.

#### GET /monitoring/logs
Get application logs.

**Query Parameters:**
- `level`: Log level (debug, info, warn, error)
- `start`: Start timestamp
- `end`: End timestamp
- `limit`: Number of logs to return

### File Upload Endpoints

#### POST /upload
Upload file to cloud storage.

**Request:** Multipart form data
- `file`: File to upload
- `category`: File category (avatar, document, image)
- `metadata`: Additional metadata (JSON string)

**Response:**
```json
{
  "success": true,
  "data": {
    "fileId": "file_123",
    "url": "https://storage.example.com/files/file_123.jpg",
    "size": 1024000,
    "mimeType": "image/jpeg"
  }
}
```

#### GET /files/:id
Get file information.

#### DELETE /files/:id
Delete file.

## Error Codes

| Code | Description |
|------|-------------|
| `AUTH_REQUIRED` | Authentication required |
| `AUTH_INVALID` | Invalid authentication token |
| `AUTH_EXPIRED` | Authentication token expired |
| `PERMISSION_DENIED` | Insufficient permissions |
| `VALIDATION_ERROR` | Request validation failed |
| `RESOURCE_NOT_FOUND` | Requested resource not found |
| `RATE_LIMIT_EXCEEDED` | Rate limit exceeded |
| `INTERNAL_ERROR` | Internal server error |
| `SERVICE_UNAVAILABLE` | External service unavailable |

## Rate Limiting

API requests are rate limited per user/IP:

- **Authentication endpoints**: 5 requests per minute
- **General API**: 100 requests per minute
- **File upload**: 10 requests per minute
- **AI endpoints**: 20 requests per minute

Rate limit headers are included in responses:
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640995200
```

## Webhooks

The API supports webhooks for real-time notifications:

### Webhook Events
- `user.created`
- `user.updated`
- `workflow.executed`
- `workflow.failed`
- `ai.chat.completed`
- `file.uploaded`

### Webhook Payload
```json
{
  "event": "user.created",
  "timestamp": "2024-01-01T00:00:00Z",
  "data": {
    "userId": "user_123",
    "email": "user@example.com"
  }
}
```

## SDKs and Libraries

Official SDKs are available for:
- JavaScript/TypeScript
- Python
- Go
- Java
- PHP

## Support

For API support:
- Email: api-support@devtechai.org
- Documentation: https://docs.devtechai.org/api
- Status Page: https://status.devtechai.org
