// Authentication Service Interfaces
export interface AuthProvider {
  authenticate(credentials: AuthCredentials): Promise<AuthResult>;
  refreshToken(refreshToken: string): Promise<AuthResult>;
  logout(token: string): Promise<void>;
  validateToken(token: string): Promise<TokenValidation>;
}

export interface AuthCredentials {
  email: string;
  password: string;
  provider?: string;
}

export interface AuthResult {
  accessToken: string;
  refreshToken: string;
  expiresIn: number;
  user: User;
}

export interface TokenValidation {
  valid: boolean;
  user?: User;
  expiresAt?: Date;
}

export interface User {
  id: string;
  email: string;
  name: string;
  roles: string[];
  permissions: string[];
  createdAt: Date;
  updatedAt: Date;
  lastLoginAt?: Date;
}

// Auth0 Service Implementation
export class Auth0Service implements AuthProvider {
  private managementClient: ManagementClient;
  private auth0Client: Auth0Client;

  constructor(config: Auth0Config) {
    this.managementClient = new ManagementClient({
      domain: config.domain,
      clientId: config.clientId,
      clientSecret: config.clientSecret
    });

    this.auth0Client = new Auth0Client({
      domain: config.domain,
      clientId: config.clientId
    });
  }

  async authenticate(credentials: AuthCredentials): Promise<AuthResult> {
    try {
      const response = await this.auth0Client.passwordGrant({
        username: credentials.email,
        password: credentials.password,
        scope: 'openid profile email'
      });

      const user = await this.getUser(response.access_token);

      return {
        accessToken: response.access_token,
        refreshToken: response.refresh_token,
        expiresIn: response.expires_in,
        user: this.mapUser(user)
      };
    } catch (error) {
      throw new AuthenticationError('Invalid credentials', error);
    }
  }

  async refreshToken(refreshToken: string): Promise<AuthResult> {
    try {
      const response = await this.auth0Client.refreshToken({
        refresh_token: refreshToken
      });

      const user = await this.getUser(response.access_token);

      return {
        accessToken: response.access_token,
        refreshToken: response.refresh_token,
        expiresIn: response.expires_in,
        user: this.mapUser(user)
      };
    } catch (error) {
      throw new AuthenticationError('Invalid refresh token', error);
    }
  }

  async logout(token: string): Promise<void> {
    try {
      await this.auth0Client.logout({
        token
      });
    } catch (error) {
      throw new AuthenticationError('Logout failed', error);
    }
  }

  async validateToken(token: string): Promise<TokenValidation> {
    try {
      const user = await this.auth0Client.getUser(token);
      return {
        valid: true,
        user: this.mapUser(user),
        expiresAt: new Date(user.exp * 1000)
      };
    } catch (error) {
      return { valid: false };
    }
  }

  private async getUser(token: string): Promise<any> {
    return this.auth0Client.getUser(token);
  }

  private mapUser(auth0User: any): User {
    return {
      id: auth0User.sub,
      email: auth0User.email,
      name: auth0User.name,
      roles: auth0User['https://devtechai.org/roles'] || [],
      permissions: auth0User['https://devtechai.org/permissions'] || [],
      createdAt: new Date(auth0User.created_at),
      updatedAt: new Date(auth0User.updated_at),
      lastLoginAt: new Date()
    };
  }
}

// Firebase Auth Service Implementation
export class FirebaseAuthService implements AuthProvider {
  private auth: Auth;

  constructor(config: FirebaseConfig) {
    const app = initializeApp(config);
    this.auth = getAuth(app);
  }

  async authenticate(credentials: AuthCredentials): Promise<AuthResult> {
    try {
      const userCredential = await signInWithEmailAndPassword(
        this.auth,
        credentials.email,
        credentials.password
      );

      const token = await userCredential.user.getIdToken();
      const refreshToken = await userCredential.user.getIdToken(true);

      return {
        accessToken: token,
        refreshToken: refreshToken,
        expiresIn: 3600,
        user: this.mapUser(userCredential.user)
      };
    } catch (error) {
      throw new AuthenticationError('Invalid credentials', error);
    }
  }

  async refreshToken(refreshToken: string): Promise<AuthResult> {
    try {
      const user = this.auth.currentUser;
      if (!user) {
        throw new AuthenticationError('No user found');
      }

      const token = await user.getIdToken(true);

      return {
        accessToken: token,
        refreshToken: token,
        expiresIn: 3600,
        user: this.mapUser(user)
      };
    } catch (error) {
      throw new AuthenticationError('Token refresh failed', error);
    }
  }

  async logout(token: string): Promise<void> {
    try {
      await this.auth.signOut();
    } catch (error) {
      throw new AuthenticationError('Logout failed', error);
    }
  }

  async validateToken(token: string): Promise<TokenValidation> {
    try {
      const decodedToken = await this.auth.verifyIdToken(token);
      return {
        valid: true,
        user: this.mapUserFromToken(decodedToken),
        expiresAt: new Date(decodedToken.exp * 1000)
      };
    } catch (error) {
      return { valid: false };
    }
  }

  private mapUser(firebaseUser: any): User {
    return {
      id: firebaseUser.uid,
      email: firebaseUser.email,
      name: firebaseUser.displayName || firebaseUser.email,
      roles: firebaseUser.customClaims?.roles || [],
      permissions: firebaseUser.customClaims?.permissions || [],
      createdAt: new Date(firebaseUser.metadata.creationTime),
      updatedAt: new Date(firebaseUser.metadata.lastSignInTime),
      lastLoginAt: new Date()
    };
  }

  private mapUserFromToken(token: any): User {
    return {
      id: token.uid,
      email: token.email,
      name: token.name || token.email,
      roles: token.roles || [],
      permissions: token.permissions || [],
      createdAt: new Date(token.iat * 1000),
      updatedAt: new Date(token.iat * 1000),
      lastLoginAt: new Date(token.auth_time * 1000)
    };
  }
}

// Custom JWT Service Implementation
export class CustomJWTAuthService implements AuthProvider {
  private jwtSecret: string;
  private jwtExpiresIn: string;
  private refreshExpiresIn: string;

  constructor(config: JWTConfig) {
    this.jwtSecret = config.secret;
    this.jwtExpiresIn = config.expiresIn;
    this.refreshExpiresIn = config.refreshExpiresIn;
  }

  async authenticate(credentials: AuthCredentials): Promise<AuthResult> {
    try {
      // Validate credentials against database
      const user = await this.validateCredentials(credentials);
      
      const accessToken = jwt.sign(
        { userId: user.id, email: user.email },
        this.jwtSecret,
        { expiresIn: this.jwtExpiresIn }
      );

      const refreshToken = jwt.sign(
        { userId: user.id, type: 'refresh' },
        this.jwtSecret,
        { expiresIn: this.refreshExpiresIn }
      );

      return {
        accessToken,
        refreshToken,
        expiresIn: 900, // 15 minutes
        user
      };
    } catch (error) {
      throw new AuthenticationError('Invalid credentials', error);
    }
  }

  async refreshToken(refreshToken: string): Promise<AuthResult> {
    try {
      const decoded = jwt.verify(refreshToken, this.jwtSecret) as any;
      
      if (decoded.type !== 'refresh') {
        throw new AuthenticationError('Invalid refresh token');
      }

      const user = await this.getUserById(decoded.userId);
      
      const newAccessToken = jwt.sign(
        { userId: user.id, email: user.email },
        this.jwtSecret,
        { expiresIn: this.jwtExpiresIn }
      );

      return {
        accessToken: newAccessToken,
        refreshToken,
        expiresIn: 900,
        user
      };
    } catch (error) {
      throw new AuthenticationError('Invalid refresh token', error);
    }
  }

  async logout(token: string): Promise<void> {
    try {
      // Add token to blacklist
      await this.blacklistToken(token);
    } catch (error) {
      throw new AuthenticationError('Logout failed', error);
    }
  }

  async validateToken(token: string): Promise<TokenValidation> {
    try {
      const decoded = jwt.verify(token, this.jwtSecret) as any;
      
      // Check if token is blacklisted
      if (await this.isTokenBlacklisted(token)) {
        return { valid: false };
      }

      const user = await this.getUserById(decoded.userId);
      
      return {
        valid: true,
        user,
        expiresAt: new Date(decoded.exp * 1000)
      };
    } catch (error) {
      return { valid: false };
    }
  }

  private async validateCredentials(credentials: AuthCredentials): Promise<User> {
    // Implementation depends on your database service
    throw new Error('Not implemented');
  }

  private async getUserById(userId: string): Promise<User> {
    // Implementation depends on your database service
    throw new Error('Not implemented');
  }

  private async blacklistToken(token: string): Promise<void> {
    // Implementation depends on your cache service
    throw new Error('Not implemented');
  }

  private async isTokenBlacklisted(token: string): Promise<boolean> {
    // Implementation depends on your cache service
    throw new Error('Not implemented');
  }
}

// Authentication Factory
export class AuthServiceFactory {
  static createService(type: string, config: any): AuthProvider {
    switch (type) {
      case 'auth0':
        return new Auth0Service(config);
      case 'firebase':
        return new FirebaseAuthService(config);
      case 'jwt':
        return new CustomJWTAuthService(config);
      default:
        throw new Error(`Unknown auth provider: ${type}`);
    }
  }
}

// Custom Error Classes
export class AuthenticationError extends Error {
  constructor(message: string, cause?: Error) {
    super(message);
    this.name = 'AuthenticationError';
    this.cause = cause;
  }
}

export class AuthorizationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'AuthorizationError';
  }
}

// Configuration Interfaces
export interface Auth0Config {
  domain: string;
  clientId: string;
  clientSecret: string;
}

export interface FirebaseConfig {
  apiKey: string;
  authDomain: string;
  projectId: string;
}

export interface JWTConfig {
  secret: string;
  expiresIn: string;
  refreshExpiresIn: string;
}
