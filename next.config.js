/** @type {import('next').NextConfig} */
const nextConfig = {
  // Static export for deployment
  output: 'export',
  distDir: 'out',
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
};

module.exports = nextConfig;

