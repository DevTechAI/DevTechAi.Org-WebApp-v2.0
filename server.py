#!/usr/bin/env python3
"""
Simple HTTP Server for DevTechAI WebApp v2.0
Serves the static files and handles basic routing
"""

import http.server
import socketserver
import os
import sys
from urllib.parse import urlparse, parse_qs
import json

class DevTechAIHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        # Handle API endpoints
        if parsed_path.path.startswith('/api/'):
            self.handle_api_request(parsed_path)
            return
        
        # Serve static files
        super().do_GET()
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        
        # Handle API endpoints
        if parsed_path.path.startswith('/api/'):
            self.handle_api_request(parsed_path)
            return
        
        # Handle form submissions
        if parsed_path.path in ['/forms/contact.php', '/forms/newsletter.php']:
            self.handle_form_submission(parsed_path)
            return
        
        super().do_POST()
    
    def handle_api_request(self, parsed_path):
        """Handle API requests"""
        path = parsed_path.path
        
        if path == '/api/health':
            self.send_json_response({'status': 'healthy', 'message': 'DevTechAI WebApp v2.0 is running'})
        elif path == '/api/services':
            services = [
                {'id': 1, 'name': 'AI Integration', 'description': 'Integrate OpenAI, Anthropic, Google AI, and Azure AI services'},
                {'id': 2, 'name': 'Workflow Automation', 'description': 'Automate processes using N8N, Zapier, and custom solutions'},
                {'id': 3, 'name': 'Cloud Solutions', 'description': 'Deploy across AWS, GCP, OCI, and Azure platforms'},
                {'id': 4, 'name': 'Monitoring & Analytics', 'description': 'Comprehensive monitoring with Prometheus and Grafana'},
                {'id': 5, 'name': 'Security & Compliance', 'description': 'Enterprise-grade security with GDPR, CCPA, HIPAA compliance'},
                {'id': 6, 'name': 'API Development', 'description': 'Build robust APIs with comprehensive documentation'}
            ]
            self.send_json_response({'services': services})
        elif path == '/api/team':
            team = [
                {'id': 1, 'name': 'Alex Johnson', 'position': 'Chief Executive Officer', 'image': 'assets/img/team/team-1.jpg'},
                {'id': 2, 'name': 'Sarah Chen', 'position': 'Chief Technology Officer', 'image': 'assets/img/team/team-2.jpg'},
                {'id': 3, 'name': 'Michael Rodriguez', 'position': 'AI Solutions Architect', 'image': 'assets/img/team/team-3.jpg'},
                {'id': 4, 'name': 'Emily Davis', 'position': 'Cloud Infrastructure Lead', 'image': 'assets/img/team/team-4.jpg'}
            ]
            self.send_json_response({'team': team})
        else:
            self.send_error(404, "API endpoint not found")
    
    def handle_form_submission(self, parsed_path):
        """Handle form submissions"""
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        if parsed_path.path == '/forms/contact.php':
            # Simulate contact form processing
            self.send_json_response({
                'status': 'success',
                'message': 'Your message has been sent successfully. We will get back to you soon!'
            })
        elif parsed_path.path == '/forms/newsletter.php':
            # Simulate newsletter subscription
            self.send_json_response({
                'status': 'success',
                'message': 'Thank you for subscribing to our newsletter!'
            })
    
    def send_json_response(self, data):
        """Send JSON response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def log_message(self, format, *args):
        """Custom log message format"""
        sys.stderr.write(f"[DevTechAI Server] {format % args}\n")

def main():
    """Main function to start the server"""
    PORT = 8000
    
    # Check if port is available
    try:
        with socketserver.TCPServer(("", PORT), DevTechAIHandler) as httpd:
            print(f"🚀 DevTechAI WebApp v2.0 Server starting...")
            print(f"📡 Server running at http://localhost:{PORT}")
            print(f"📁 Serving files from: {os.getcwd()}")
            print(f"🔗 Open your browser and visit: http://localhost:{PORT}")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 60)
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n🛑 Server stopped by user")
                httpd.shutdown()
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Please try a different port.")
            print(f"💡 You can specify a different port by modifying the PORT variable in this script.")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
