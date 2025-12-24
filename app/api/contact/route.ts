import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    let body: any;
    
    // Handle both JSON and form-encoded data
    const contentType = request.headers.get('content-type');
    
    if (contentType?.includes('application/json')) {
      body = await request.json();
    } else if (contentType?.includes('application/x-www-form-urlencoded')) {
      const formData = await request.formData();
      body = {
        name: formData.get('name') as string,
        email: formData.get('email') as string,
        subject: formData.get('subject') as string,
        message: formData.get('message') as string,
      };
    } else {
      // Try to parse as form data by default
      const formData = await request.formData();
      body = {
        name: formData.get('name') as string,
        email: formData.get('email') as string,
        subject: formData.get('subject') as string,
        message: formData.get('message') as string,
      };
    }
    
    console.log('📨 Next.js API received:', body);
    
    // Forward the request to our Express API server
    const response = await fetch('http://localhost:8001/api/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body)
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      console.log('❌ Express API error:', data);
      return NextResponse.json(data, { status: response.status });
    }
    
    console.log('✅ Success from Express API:', data);
    return NextResponse.json(data);
    
  } catch (error: any) {
    console.error('❌ Next.js API proxy error:', error);
    return NextResponse.json(
      { error: 'Internal Server Error', message: 'Failed to submit contact form' },
      { status: 500 }
    );
  }
}
