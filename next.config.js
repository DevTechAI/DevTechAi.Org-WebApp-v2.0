const isProd = process.env.NODE_ENV === 'production';

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Static export for deployment (only in production)
  output: isProd ? 'export' : undefined,
  distDir: isProd ? 'out' : undefined,
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
  // Skip TypeScript and ESLint checks during build for faster deployment
  typescript: {
    ignoreBuildErrors: true,
  },
  eslint: {
    ignoreDuringBuilds: true,
  },
  // Rewrite routes to static HTML files
  async rewrites() {
    if (isProd) return [];
    return [
      {
        source: '/',
        destination: '/index.html',
      },
      // Handle services routes
      {
        source: '/services/:path*',
        destination: '/services/:path*',
      },
      // Handle portfolio routes
      {
        source: '/portfolio/:path*',
        destination: '/portfolio/:path*',
      },
      // Handle solutions routes
      {
        source: '/solutions/:path*',
        destination: '/solutions/:path*',
      },
    ];
  },
};

module.exports = nextConfig;

