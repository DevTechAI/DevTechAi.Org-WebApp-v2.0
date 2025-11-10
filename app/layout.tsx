import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'DevTechAI.Org - AI-Powered Solutions',
  description: 'FullStack Apps modernization with GenAI, AgenticAI multi-model features',
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

