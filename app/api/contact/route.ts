import { createClient } from '@supabase/supabase-js';
import { NextRequest, NextResponse } from 'next/server';

const supabase = createClient(
  process.env.SUPABASE_URL || '',
  process.env.SUPABASE_ANON_KEY || ''
);

export async function POST(request: NextRequest) {
  try {
    const contentType = request.headers.get('content-type') || '';
    let body: any = {};

    if (contentType.includes('application/json')) {
      body = await request.json();
    } else {
      // support form submissions (application/x-www-form-urlencoded or multipart/form-data)
      try {
        const form = await request.formData();
        body = Object.fromEntries(form.entries());
      } catch (e) {
        try {
          body = await request.json();
        } catch (_) {
          body = {};
        }
      }
    }

    const name = (body.name || '').toString();
    const email = (body.email || '').toString();
    const subject = (body.subject || '').toString();
    const message = (body.message || '').toString();

    const isXhr = (request.headers.get('x-requested-with') || '').toLowerCase() === 'xmlhttprequest';

    if (!name || !email || !message) {
      const errMsg = 'name, email and message are required';
      if (isXhr) return new Response(errMsg, { status: 400, headers: { 'Content-Type': 'text/plain' } });
      return NextResponse.json({ error: errMsg }, { status: 400 });
    }

    const { data, error } = await supabase
      .from('contacts')
      .insert([{ name, email, subject, message }])
      .select();

    if (error) {
      console.error('Supabase insert error:', error);
      const errMsg = 'Failed to save contact';
      if (isXhr) return new Response(errMsg, { status: 500, headers: { 'Content-Type': 'text/plain' } });
      return NextResponse.json({ error: errMsg }, { status: 500 });
    }

    if (isXhr) {
      // php-email-form expects plain text 'OK' on success
      return new Response('OK', { status: 200, headers: { 'Content-Type': 'text/plain' } });
    }

    return NextResponse.json({ message: 'Contact saved', data }, { status: 200 });
  } catch (err) {
    console.error('API error:', err);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
