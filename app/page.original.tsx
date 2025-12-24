/**
 * Next.js App Router Root Page
 * Client-side redirect to static index.html
 * The static HTML site is served from the public directory
 */

'use client';

import { useEffect } from 'react';

export default function Home() {
  useEffect(() => {
    // Client-side redirect to static index.html
    window.location.href = '/index.html';
  }, []);

  return (
    <div style={{ 
      display: 'flex', 
      justifyContent: 'center', 
      alignItems: 'center', 
      height: '100vh',
      flexDirection: 'column',
      gap: '1rem'
    }}>
      <h1>DevTechAI.Org</h1>
      <p>Loading...</p>
    </div>
  );
}

