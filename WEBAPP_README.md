# DevTechAI WebApp v2.0

A comprehensive web application built with modern technologies, featuring AI integration, workflow automation, cloud services, and enterprise-grade monitoring.

## 🚀 Quick Start

### Prerequisites

- Python 3.7+ (for the development server)
- Node.js 18+ (for the full application)
- Modern web browser

### Running the WebApp

1. **Simple Static Server (Recommended for UI testing):**
   ```bash
   # Start the Python development server
   npm run start:webapp
   # or
   python3 server.py
   # or
   ./start.sh
   ```

2. **Full Application (with backend services):**
   ```bash
   # Install dependencies
   npm install
   
   # Start development environment
   npm run dev
   ```

3. **Access the application:**
   - Open your browser and visit: `http://localhost:8000`
   - The webapp will be fully functional with all animations and interactions

## 📁 Project Structure

```
DevTechAi.Org-WebApp-v2.0/
├── index.html              # Main webapp page
├── server.py               # Python development server
├── start.sh                # Startup script
├── assets/                 # Static assets (CSS, JS, images)
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   ├── img/               # Images and media
│   └── vendor/            # Third-party libraries
├── src/                    # Source code for full application
├── docs/                   # Documentation
├── infrastructure/         # Infrastructure as Code
├── monitoring/            # Monitoring configurations
├── security/              # Security policies
└── workflows/             # Workflow definitions
```

## 🎨 Features

### Current WebApp Features
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI**: Clean, professional interface with smooth animations
- **Interactive Elements**: 
  - Smooth scrolling navigation
  - Animated counters and statistics
  - Image galleries with lightbox
  - Swiper carousels for testimonials and clients
  - Isotope filtering for portfolio
- **Contact Forms**: Functional contact and newsletter forms
- **API Endpoints**: Basic API for services, team, and health checks

### Planned Features (Full Application)
- **AI Integration**: OpenAI, Anthropic, Google AI, Azure AI
- **Workflow Automation**: N8N, Zapier, custom workflows
- **Cloud Services**: AWS, GCP, OCI, Azure support
- **Database Integration**: Supabase, Firebase, PostgreSQL
- **Authentication**: Auth0, Firebase Auth, custom auth
- **Monitoring**: Prometheus, Grafana, comprehensive logging
- **Security**: Enterprise-grade security and compliance

## 🛠️ Development

### WebApp Development
The current webapp is a static site that can be easily customized:

1. **Styling**: Modify `assets/css/main.css` for custom styles
2. **Content**: Update `index.html` for content changes
3. **Images**: Replace images in `assets/img/` directory
4. **Functionality**: Extend `server.py` for additional API endpoints

### Full Application Development
For the complete application with backend services:

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

## 🌐 API Endpoints

The development server provides these API endpoints:

- `GET /api/health` - Health check
- `GET /api/services` - List of services
- `GET /api/team` - Team members
- `POST /forms/contact.php` - Contact form submission
- `POST /forms/newsletter.php` - Newsletter subscription

## 📱 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🔧 Customization

### Changing Colors
Edit the CSS variables in `assets/css/main.css`:

```css
:root {
  --accent-color: #ffc451;        /* Primary brand color */
  --heading-color: #151515;       /* Headings color */
  --default-color: #444444;       /* Text color */
  --background-color: #ffffff;    /* Background color */
}
```

### Adding New Sections
1. Add HTML structure in `index.html`
2. Add corresponding styles in `assets/css/main.css`
3. Update navigation menu if needed

### Adding New API Endpoints
Extend the `handle_api_request` method in `server.py`:

```python
elif path == '/api/your-endpoint':
    data = {'message': 'Your response'}
    self.send_json_response(data)
```

## 📄 License

This project is proprietary software owned by DevTechAI.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For support and questions:
- Email: info@devtechai.org
- Documentation: See `docs/` directory
- Issues: Create an issue in the repository

---

**DevTechAI WebApp v2.0** - Empowering businesses with AI-driven solutions.
