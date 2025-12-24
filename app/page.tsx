/**
 * Next.js App Router Root Page
 * Server-side redirect to static index.html
 * The static HTML site is served from the public directory
 */

import { redirect } from 'next/navigation';

export default function Home() {
  // Server-side redirect to the main site
  redirect('/index.html');
}
