import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'DevTechAi.Org',
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
