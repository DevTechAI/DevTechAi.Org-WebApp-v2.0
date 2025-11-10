/**
 * Next.js App Router Root Page
 * Minimal Next.js app structure for Vercel deployment
 * This allows Next.js build to succeed while serving static files
 */

import { redirect } from 'next/navigation';

export default function Home() {
  // Server-side redirect to static index.html
  redirect('/index.html');
}

