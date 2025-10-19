# Monitoring & Observability

## Overview

The DevTechAI WebApp v2.0 implements a comprehensive monitoring and observability stack to ensure system reliability, performance, and security.

## Monitoring Architecture

### Three Pillars of Observability
- **Metrics**: Quantitative measurements of system behavior
- **Logs**: Detailed records of events and activities
- **Traces**: Request flow through distributed systems

### Monitoring Stack
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Applications  │    │   Infrastructure │    │   External      │
│                 │    │                 │    │   Services      │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          ▼                      ▼                      ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Prometheus     │    │   Grafana       │    │   AlertManager  │
│   (Metrics)      │    │   (Dashboards)  │    │   (Alerts)      │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 ▼
                    ┌─────────────────┐
                    │   ELK Stack     │
                    │   (Logging)     │
                    └─────────────────┘
```

## Metrics Collection

### Application Metrics
```typescript
// Custom Business Metrics
import { register, Counter, Histogram, Gauge } from 'prom-client';

// Request Counter
const httpRequestCounter = new Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code']
});

// Response Time Histogram
const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route'],
  buckets: [0.1, 0.5, 1, 2, 5, 10]
});

// Active Users Gauge
const activeUsersGauge = new Gauge({
  name: 'active_users_total',
  help: 'Number of active users'
});

// Register metrics
register.registerMetric(httpRequestCounter);
register.registerMetric(httpRequestDuration);
register.registerMetric(activeUsersGauge);
```

### Infrastructure Metrics
- **CPU Usage**: Per-node and per-pod CPU utilization
- **Memory Usage**: Memory consumption and limits
- **Disk Usage**: Storage utilization and I/O
- **Network**: Bandwidth and packet statistics
- **Kubernetes**: Pod, service, and deployment metrics

### Database Metrics
```typescript
// Database Performance Metrics
const dbQueryDuration = new Histogram({
  name: 'database_query_duration_seconds',
  help: 'Duration of database queries',
  labelNames: ['query_type', 'table'],
  buckets: [0.01, 0.05, 0.1, 0.5, 1, 2, 5]
});

const dbConnections = new Gauge({
  name: 'database_connections_active',
  help: 'Number of active database connections'
});

const dbTransactions = new Counter({
  name: 'database_transactions_total',
  help: 'Total number of database transactions',
  labelNames: ['type', 'status']
});
```

## Logging Strategy

### Structured Logging
```typescript
import winston from 'winston';

// Logger Configuration
const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'devtechai-app' },
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' }),
    new winston.transports.Console({
      format: winston.format.simple()
    })
  ]
});

// Request Logging Middleware
export const requestLogger = (req: Request, res: Response, next: NextFunction) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = Date.now() - start;
    logger.info('HTTP Request', {
      method: req.method,
      url: req.url,
      statusCode: res.statusCode,
      duration,
      userAgent: req.get('User-Agent'),
      ip: req.ip,
      userId: req.user?.id
    });
  });
  
  next();
};
```

### Log Levels
- **ERROR**: System errors and exceptions
- **WARN**: Warning conditions
- **INFO**: General information
- **DEBUG**: Detailed debugging information
- **TRACE**: Very detailed tracing

### Log Aggregation
```yaml
# Fluentd Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluentd-config
data:
  fluent.conf: |
    <source>
      @type tail
      path /var/log/containers/*.log
      pos_file /var/log/fluentd-containers.log.pos
      tag kubernetes.*
      format json
    </source>
    
    <match kubernetes.**>
      @type elasticsearch
      host elasticsearch.logging.svc.cluster.local
      port 9200
      index_name devtechai-logs
    </match>
```

## Distributed Tracing

### OpenTelemetry Integration
```typescript
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';

// Initialize OpenTelemetry
const sdk = new NodeSDK({
  traceExporter: new JaegerExporter({
    endpoint: 'http://jaeger:14268/api/traces'
  }),
  instrumentations: [getNodeAutoInstrumentations()]
});

sdk.start();

// Custom Tracing
import { trace } from '@opentelemetry/api';

const tracer = trace.getTracer('devtechai-app');

export const traceFunction = async <T>(
  name: string,
  fn: () => Promise<T>
): Promise<T> => {
  const span = tracer.startSpan(name);
  try {
    const result = await fn();
    span.setStatus({ code: SpanStatusCode.OK });
    return result;
  } catch (error) {
    span.setStatus({ 
      code: SpanStatusCode.ERROR, 
      message: error.message 
    });
    throw error;
  } finally {
    span.end();
  }
};
```

### Trace Context Propagation
```typescript
// Trace Context Middleware
export const traceMiddleware = (req: Request, res: Response, next: NextFunction) => {
  const traceId = req.headers['x-trace-id'] as string;
  const spanId = req.headers['x-span-id'] as string;
  
  if (traceId && spanId) {
    const spanContext = {
      traceId,
      spanId,
      traceFlags: TraceFlags.SAMPLED
    };
    
    const context = trace.setSpanContext(ROOT_CONTEXT, spanContext);
    trace.setGlobalContextManager(context);
  }
  
  next();
};
```

## Alerting System

### Alert Rules
```yaml
# Prometheus Alert Rules
groups:
- name: devtechai-alerts
  rules:
  - alert: HighErrorRate
    expr: rate(http_requests_total{status_code=~"5.."}[5m]) > 0.1
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "High error rate detected"
      description: "Error rate is {{ $value }} errors per second"
  
  - alert: HighResponseTime
    expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High response time"
      description: "95th percentile response time is {{ $value }} seconds"
  
  - alert: DatabaseConnectionsHigh
    expr: database_connections_active > 80
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: "High database connections"
      description: "Database connections: {{ $value }}"
```

### AlertManager Configuration
```yaml
# AlertManager Config
global:
  smtp_smarthost: 'smtp.gmail.com:587'
  smtp_from: 'alerts@devtechai.org'

route:
  group_by: ['alertname']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'web.hook'

receivers:
- name: 'web.hook'
  webhook_configs:
  - url: 'http://slack-webhook:5001/'
    send_resolved: true

- name: 'email'
  email_configs:
  - to: 'ops@devtechai.org'
    subject: 'DevTechAI Alert: {{ .GroupLabels.alertname }}'
    body: |
      {{ range .Alerts }}
      Alert: {{ .Annotations.summary }}
      Description: {{ .Annotations.description }}
      {{ end }}
```

## Dashboards

### Grafana Dashboard Configuration
```json
{
  "dashboard": {
    "title": "DevTechAI Application Metrics",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} {{route}}"
          }
        ]
      },
      {
        "title": "Response Time",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "95th percentile"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "singlestat",
        "targets": [
          {
            "expr": "rate(http_requests_total{status_code=~\"5..\"}[5m])",
            "format": "percent"
          }
        ]
      }
    ]
  }
}
```

### Custom Dashboards
- **Application Overview**: Key application metrics
- **Infrastructure**: System resource utilization
- **Database**: Database performance metrics
- **Security**: Security events and alerts
- **Business Metrics**: User engagement and revenue

## Performance Monitoring

### Application Performance Monitoring (APM)
```typescript
// Performance Monitoring
import { performance } from 'perf_hooks';

export const performanceMiddleware = (req: Request, res: Response, next: NextFunction) => {
  const start = performance.now();
  
  res.on('finish', () => {
    const duration = performance.now() - start;
    
    // Record performance metrics
    httpRequestDuration.observe(
      { method: req.method, route: req.route?.path },
      duration / 1000
    );
    
    // Log slow requests
    if (duration > 1000) {
      logger.warn('Slow request detected', {
        method: req.method,
        url: req.url,
        duration,
        userId: req.user?.id
      });
    }
  });
  
  next();
};
```

### Real User Monitoring (RUM)
```typescript
// Client-side Performance Monitoring
const rumConfig = {
  applicationId: 'devtechai-app',
  apiKey: process.env.DATADOG_API_KEY,
  site: 'datadoghq.com',
  service: 'devtechai-frontend',
  env: process.env.NODE_ENV,
  version: process.env.APP_VERSION
};

// Web Vitals Tracking
const trackWebVitals = () => {
  import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
    getCLS(sendToAnalytics);
    getFID(sendToAnalytics);
    getFCP(sendToAnalytics);
    getLCP(sendToAnalytics);
    getTTFB(sendToAnalytics);
  });
};
```

## Error Tracking

### Sentry Integration
```typescript
import * as Sentry from '@sentry/node';
import { nodeProfilingIntegration } from '@sentry/profiling-node';

// Initialize Sentry
Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  integrations: [
    nodeProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
  profilesSampleRate: 1.0,
});

// Error Handling Middleware
export const errorHandler = (error: Error, req: Request, res: Response, next: NextFunction) => {
  // Capture exception
  Sentry.captureException(error);
  
  // Log error
  logger.error('Unhandled error', {
    error: error.message,
    stack: error.stack,
    url: req.url,
    method: req.method,
    userId: req.user?.id
  });
  
  // Send response
  res.status(500).json({
    success: false,
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An internal error occurred'
    }
  });
};
```

### Custom Error Tracking
```typescript
// Error Classification
enum ErrorType {
  VALIDATION = 'validation',
  AUTHENTICATION = 'authentication',
  AUTHORIZATION = 'authorization',
  DATABASE = 'database',
  EXTERNAL_SERVICE = 'external_service',
  BUSINESS_LOGIC = 'business_logic'
}

// Error Tracking Service
export class ErrorTrackingService {
  static trackError(error: Error, context: any) {
    const errorInfo = {
      message: error.message,
      stack: error.stack,
      type: this.classifyError(error),
      context,
      timestamp: new Date().toISOString(),
      userId: context.userId,
      requestId: context.requestId
    };
    
    // Send to monitoring service
    this.sendToMonitoring(errorInfo);
    
    // Log locally
    logger.error('Error tracked', errorInfo);
  }
  
  private static classifyError(error: Error): ErrorType {
    if (error.name === 'ValidationError') return ErrorType.VALIDATION;
    if (error.name === 'AuthenticationError') return ErrorType.AUTHENTICATION;
    if (error.name === 'AuthorizationError') return ErrorType.AUTHORIZATION;
    if (error.name === 'DatabaseError') return ErrorType.DATABASE;
    return ErrorType.BUSINESS_LOGIC;
  }
}
```

## Health Checks

### Application Health Checks
```typescript
// Health Check Endpoint
export const healthCheck = async (req: Request, res: Response) => {
  const health = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    version: process.env.APP_VERSION,
    uptime: process.uptime(),
    services: {}
  };
  
  // Check database
  try {
    await prisma.$queryRaw`SELECT 1`;
    health.services.database = 'healthy';
  } catch (error) {
    health.services.database = 'unhealthy';
    health.status = 'unhealthy';
  }
  
  // Check Redis
  try {
    await redis.ping();
    health.services.redis = 'healthy';
  } catch (error) {
    health.services.redis = 'unhealthy';
    health.status = 'unhealthy';
  }
  
  // Check external services
  for (const service of externalServices) {
    try {
      await service.healthCheck();
      health.services[service.name] = 'healthy';
    } catch (error) {
      health.services[service.name] = 'unhealthy';
      health.status = 'unhealthy';
    }
  }
  
  const statusCode = health.status === 'healthy' ? 200 : 503;
  res.status(statusCode).json(health);
};
```

### Kubernetes Health Checks
```yaml
# Kubernetes Health Checks
apiVersion: apps/v1
kind: Deployment
metadata:
  name: devtechai-app
spec:
  template:
    spec:
      containers:
      - name: app
        image: devtechai/app:latest
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
```

## Monitoring Tools Integration

### Datadog Integration
```typescript
// Datadog Configuration
import { StatsD } from 'node-statsd';

const datadog = new StatsD({
  host: 'datadog-agent',
  port: 8125,
  prefix: 'devtechai.'
});

// Custom Metrics
export const trackCustomMetric = (name: string, value: number, tags: string[] = []) => {
  datadog.gauge(name, value, tags);
};

// Business Metrics
export const trackUserRegistration = (userId: string) => {
  datadog.increment('user.registration', [`user_id:${userId}`]);
};

export const trackWorkflowExecution = (workflowId: string, duration: number) => {
  datadog.timing('workflow.execution_time', duration, [`workflow_id:${workflowId}`]);
};
```

### New Relic Integration
```typescript
// New Relic Configuration
import newrelic from 'newrelic';

// Custom Attributes
export const addCustomAttributes = (attributes: Record<string, any>) => {
  Object.entries(attributes).forEach(([key, value]) => {
    newrelic.addCustomAttribute(key, value);
  });
};

// Custom Events
export const recordCustomEvent = (eventType: string, attributes: Record<string, any>) => {
  newrelic.recordCustomEvent(eventType, attributes);
};
```

## Monitoring Best Practices

### Metric Naming Conventions
- Use descriptive names: `http_request_duration_seconds`
- Include units: `_seconds`, `_bytes`, `_total`
- Use consistent prefixes: `devtechai_`, `app_`
- Avoid high cardinality labels

### Logging Best Practices
- Use structured logging (JSON)
- Include correlation IDs
- Log at appropriate levels
- Avoid logging sensitive data
- Use consistent log formats

### Alerting Best Practices
- Set appropriate thresholds
- Use multiple alert channels
- Include runbook links
- Test alerting regularly
- Avoid alert fatigue

## Troubleshooting

### Common Monitoring Issues
- **Missing Metrics**: Check metric collection configuration
- **High Cardinality**: Review label usage
- **Alert Noise**: Adjust thresholds and filters
- **Performance Impact**: Monitor monitoring overhead

### Monitoring Maintenance
- Regular dashboard reviews
- Alert rule optimization
- Log retention management
- Metric cleanup
- Performance tuning
