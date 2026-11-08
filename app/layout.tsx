import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'DevTechAi.Org',
  description: 'FullStack Apps modernization with GenAI, AgenticAI multi-model features',
  icons: {
    icon: [
      { url: '/favicon.ico?v=2', sizes: 'any' },
      { url: '/images/logos/favicon-32.png?v=2', type: 'image/png', sizes: '32x32' },
      { url: '/images/logos/favicon-192.png?v=2', type: 'image/png', sizes: '192x192' },
    ],
    apple: '/images/logos/apple-touch-icon.png?v=2',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
