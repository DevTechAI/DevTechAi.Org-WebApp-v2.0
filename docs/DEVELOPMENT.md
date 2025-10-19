# Development Guide

## Getting Started

This guide will help you set up the development environment for the DevTechAI WebApp v2.0.

## Prerequisites

- **Node.js**: 18.0.0 or higher
- **npm**: 9.0.0 or higher
- **Docker**: 24.0.0 or higher
- **Docker Compose**: 2.0.0 or higher
- **Git**: 2.30.0 or higher

## Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/devtechai/webapp-v2.0.git
cd webapp-v2.0
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Environment Configuration
```bash
cp .env.example .env
```

Edit `.env` file with your configuration:
```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/devtechai"
REDIS_URL="redis://localhost:6379"

# Authentication
JWT_SECRET="your-jwt-secret"
AUTH0_DOMAIN="your-auth0-domain"
AUTH0_CLIENT_ID="your-auth0-client-id"

# AI Services
OPENAI_API_KEY="your-openai-key"
ANTHROPIC_API_KEY="your-anthropic-key"

# Cloud Services
AWS_ACCESS_KEY_ID="your-aws-key"
AWS_SECRET_ACCESS_KEY="your-aws-secret"
AWS_REGION="us-east-1"

# Monitoring
SENTRY_DSN="your-sentry-dsn"
DATADOG_API_KEY="your-datadog-key"
```

### 4. Database Setup
```bash
# Start PostgreSQL and Redis with Docker
docker-compose up -d postgres redis

# Run database migrations
npm run db:migrate

# Seed database with sample data
npm run db:seed
```

### 5. Start Development Server
```bash
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- API: http://localhost:3001
- Admin Panel: http://localhost:3000/admin

## Project Structure

```
src/
├── app/                    # Frontend application
│   ├── components/         # Reusable components
│   ├── pages/             # Page components
│   ├── hooks/             # Custom React hooks
│   ├── context/           # React context providers
│   └── utils/             # Utility functions
├── services/               # External service integrations
│   ├── auth/              # Authentication services
│   ├── database/          # Database services
│   ├── ai/                # AI/LLM services
│   ├── cloud/             # Cloud services
│   ├── workflow/          # Workflow integrations
│   ├── cicd/              # CI/CD integrations
│   └── monitoring/        # Monitoring services
├── api/                   # Backend API
│   ├── routes/            # API routes
│   ├── middleware/        # Express middleware
│   ├── controllers/       # Route controllers
│   ├── models/            # Data models
│   └── validators/        # Request validators
├── config/                # Configuration files
└── types/                 # TypeScript type definitions
```

## Development Workflow

### 1. Feature Development
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes
# Test changes
npm run test

# Commit changes
git add .
git commit -m "feat: add new feature"

# Push branch
git push origin feature/new-feature
```

### 2. Code Quality

#### Linting
```bash
npm run lint
npm run lint:fix
```

#### Type Checking
```bash
npm run type-check
```

#### Testing
```bash
# Unit tests
npm run test

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e

# Coverage report
npm run test:coverage
```

### 3. Database Operations

#### Migrations
```bash
# Create migration
npm run db:migrate:create -- --name add-user-table

# Run migrations
npm run db:migrate

# Rollback migration
npm run db:rollback
```

#### Seeding
```bash
# Seed database
npm run db:seed

# Reset database
npm run db:reset
```

## Coding Standards

### TypeScript Guidelines
- Use strict TypeScript configuration
- Define interfaces for all data structures
- Use type guards for runtime type checking
- Prefer `interface` over `type` for object shapes

### React Guidelines
- Use functional components with hooks
- Implement proper error boundaries
- Use React.memo for performance optimization
- Follow the single responsibility principle

### API Guidelines
- Use RESTful conventions
- Implement proper error handling
- Add request/response validation
- Include comprehensive logging

### Database Guidelines
- Use migrations for schema changes
- Implement proper indexing
- Use transactions for data consistency
- Follow naming conventions

## Testing Strategy

### Unit Tests
- Test individual functions and components
- Mock external dependencies
- Aim for 80%+ code coverage
- Use Jest and React Testing Library

### Integration Tests
- Test API endpoints
- Test database operations
- Test external service integrations
- Use Supertest for API testing

### End-to-End Tests
- Test complete user workflows
- Test cross-browser compatibility
- Use Playwright for E2E testing
- Run tests in CI/CD pipeline

## Debugging

### Frontend Debugging
```bash
# Enable React DevTools
npm run dev:debug

# Debug with VS Code
# Use the Debugger for Chrome extension
```

### Backend Debugging
```bash
# Enable Node.js debugging
npm run dev:debug

# Debug with VS Code
# Use the Node.js debugger
```

### Database Debugging
```bash
# Enable query logging
DEBUG=prisma:* npm run dev

# Use database GUI tools
# pgAdmin, DBeaver, or TablePlus
```

## Performance Optimization

### Frontend Optimization
- Implement code splitting
- Use lazy loading for routes
- Optimize images and assets
- Implement caching strategies

### Backend Optimization
- Use database connection pooling
- Implement Redis caching
- Optimize database queries
- Use compression middleware

### Database Optimization
- Create proper indexes
- Use query optimization
- Implement read replicas
- Monitor slow queries

## Security Best Practices

### Authentication
- Use secure JWT tokens
- Implement refresh token rotation
- Use HTTPS in production
- Validate all inputs

### Authorization
- Implement role-based access control
- Use principle of least privilege
- Validate permissions on every request
- Log all access attempts

### Data Protection
- Encrypt sensitive data
- Use environment variables for secrets
- Implement data anonymization
- Follow GDPR compliance

## Deployment

### Local Development
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Staging Deployment
```bash
# Deploy to staging
npm run deploy:staging

# Run smoke tests
npm run test:smoke
```

### Production Deployment
```bash
# Deploy to production
npm run deploy:production

# Monitor deployment
npm run monitor:deployment
```

## Troubleshooting

### Common Issues

#### Database Connection Issues
```bash
# Check database status
docker-compose ps postgres

# View database logs
docker-compose logs postgres

# Reset database
docker-compose down
docker-compose up -d postgres
```

#### Authentication Issues
```bash
# Check JWT token
npm run auth:verify-token

# Reset authentication
npm run auth:reset
```

#### Build Issues
```bash
# Clear cache
npm run clean

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### Getting Help

- Check the troubleshooting section in relevant documentation
- Search existing issues in the repository
- Create a new issue with detailed information
- Contact the development team

## Contributing

### Pull Request Process
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Code Review Process
1. Automated checks must pass
2. At least one team member review required
3. Address all review comments
4. Merge after approval

## Resources

- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React Documentation](https://react.dev/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Prisma Documentation](https://www.prisma.io/docs)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [Docker Documentation](https://docs.docker.com/)
