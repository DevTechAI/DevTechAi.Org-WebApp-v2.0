#!/usr/bin/env python3
"""Generate solution detail pages for the Solutions dropdown menu"""

import os

def generate_solution_page(title, description, content, filename, icon="bi-gear"):
    """Generate a solution detail page"""
    # Sanitize filename
    filename = filename.lower().replace(" ", "-").replace("/", "-").replace("&", "and").replace(":", "").replace(",", "")
    if not filename.endswith(".html"):
        filename += ".html"

    html_content = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{title} - DevTechAI Solutions</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="DevTechAI, {title}, solutions">

  <!-- Favicons -->
  <link href="../assets/img/favicon.png" rel="icon">
  <link href="../assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="../assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="../assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="../assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">

  <!-- Main CSS File -->
  <link href="../assets/css/main.css" rel="stylesheet">
</head>

<body class="service-details-page">

  <header id="header" class="header d-flex align-items-center position-relative">
    <div class="container-fluid container-xl position-relative d-flex align-items-center justify-content-between">

      <a href="../index.html" class="logo d-flex align-items-center me-auto me-lg-0">
        <h1 class="sitename">DevTechAI</h1>
        <span>.Org</span>
      </a>

      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="../index.html#hero">Home</a></li>
          <li><a href="../index.html#about">About</a></li>
          <li><a href="../index.html#services">Services</a></li>
          <li><a href="../index.html#portfolio">Portfolio</a></li>
          <li class="dropdown"><a href="#"><span>Solutions</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="ai-solutions.html">AI Solutions</a></li>
              <li class="dropdown"><a href="#"><span>Workflow Automation</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li><a href="n8n-integration.html">N8N Integration</a></li>
                  <li><a href="zapier-automation.html">Zapier Automation</a></li>
                  <li><a href="custom-workflows.html">Custom Workflows</a></li>
                  <li><a href="api-integrations.html">API Integrations</a></li>
                  <li><a href="webhook-management.html">Webhook Management</a></li>
                </ul>
              </li>
              <li><a href="cloud-services.html">Cloud Services</a></li>
              <li><a href="monitoring.html">Monitoring</a></li>
            </ul>
          </li>
          <li><a href="../index.html#contact">Contact</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>

      <a class="btn-getstarted" href="../index.html#about">Get Started</a>

    </div>
  </header>

  <main class="main">

    <!-- Page Title -->
    <div class="page-title" data-aos="fade">
      <div class="heading">
        <div class="container">
          <div class="row d-flex justify-content-center text-center">
            <div class="col-lg-8">
              <h1>{title}</h1>
              <p class="mb-0">{description}</p>
            </div>
          </div>
        </div>
      </div>
      <nav class="breadcrumbs">
        <div class="container">
          <ol>
            <li><a href="../index.html">Home</a></li>
            <li><a href="../index.html#services">Solutions</a></li>
            <li class="current">{title}</li>
          </ol>
        </div>
      </nav>
    </div><!-- End Page Title -->

    <!-- Solution Details Section -->
    <section id="solution-details" class="solution-details section">

      <div class="container">

        <div class="row gy-5">

          <div class="col-lg-4" data-aos="fade-up" data-aos-delay="100">

            <div class="service-box">
              <h4>Our Solutions</h4>
              <div class="services-list">
                <a href="ai-solutions.html"><i class="bi bi-arrow-right-circle"></i><span>AI Solutions</span></a>
                <a href="n8n-integration.html"><i class="bi bi-arrow-right-circle"></i><span>N8N Integration</span></a>
                <a href="zapier-automation.html"><i class="bi bi-arrow-right-circle"></i><span>Zapier Automation</span></a>
                <a href="custom-workflows.html"><i class="bi bi-arrow-right-circle"></i><span>Custom Workflows</span></a>
                <a href="api-integrations.html"><i class="bi bi-arrow-right-circle"></i><span>API Integrations</span></a>
                <a href="webhook-management.html"><i class="bi bi-arrow-right-circle"></i><span>Webhook Management</span></a>
                <a href="cloud-services.html"><i class="bi bi-arrow-right-circle"></i><span>Cloud Services</span></a>
                <a href="monitoring.html"><i class="bi bi-arrow-right-circle"></i><span>Monitoring</span></a>
              </div>
            </div>

            <div class="help-box d-flex flex-column justify-content-center align-items-center">
              <i class="bi bi-headset"></i>
              <h4>Need Help?</h4>
              <p>Our team is here to help you implement the best solutions for your business.</p>
              <a href="../index.html#contact" class="btn-get-started">Contact Us</a>
            </div>

          </div>

          <div class="col-lg-8" data-aos="fade-up" data-aos-delay="200">
            <div class="service-details">
              <div class="service-heading">
                <i class="bi bi-{icon}"></i>
                <h2>{title}</h2>
              </div>
              {content}
            </div>
          </div>

        </div>

      </div>

    </section><!-- /Solution Details Section -->

  </main>

  <footer id="footer" class="footer dark-background">

    <div class="footer-top">
      <div class="container">
        <div class="row gy-4">
          <div class="col-lg-4 col-md-6 footer-about">
            <a href="../index.html" class="logo d-flex align-items-center">
              <span class="sitename">DevTechAI.Org</span>
            </a>
            <div class="footer-contact pt-3">
              <p>4th Floor, Mani Tech Space</p>
              <p>Siddhi Vinayak Nagar, Madhapur, Hyderabad, Telangana 500081</p>
              <p class="mt-3"><strong>Email:</strong> <span>contact@devtechai.org</span></p>
              <p><strong>Phone:</strong> <span>+91 7794841440</span></p>
            </div>
            <div class="social-links d-flex mt-4">
              <a href=""><i class="bi bi-twitter-x"></i></a>
              <a href=""><i class="bi bi-facebook"></i></a>
              <a href=""><i class="bi bi-instagram"></i></a>
              <a href=""><i class="bi bi-linkedin"></i></a>
            </div>
          </div>

          <div class="col-lg-2 col-md-3 footer-links">
            <h4>Useful Links</h4>
            <ul>
              <li><i class="bi bi-chevron-right"></i> <a href="../index.html#hero"> Home</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../index.html#about"> About us</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../index.html#services"> Services</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../index.html#portfolio"> Portfolio</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../index.html#contact"> Contact</a></li>
            </ul>
          </div>

          <div class="col-lg-2 col-md-3 footer-links">
            <h4>Our Services</h4>
            <ul>
              <li><i class="bi bi-chevron-right"></i> <a href="../services/ai-modernization.html"> AI Modernization</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../services/workflow-automation.html"> Workflow Automation</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../services/cloud-ai-solutions.html"> Cloud AI Solutions</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../services/monitoring-analytics.html"> Monitoring & Analytics</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="../services/security-compliance.html"> Security & Compliance</a></li>
            </ul>
          </div>

          <div class="col-lg-4 col-md-12 footer-newsletter">
            <h4>Our Newsletter</h4>
            <p>Subscribe to our newsletter and receive the latest news about AI innovations and cloud solutions!</p>
            <form action="../forms/newsletter.php" method="post" class="php-email-form">
              <div class="newsletter-form"><input type="email" name="email"><input type="submit" value="Subscribe"></div>
              <div class="loading">Loading</div>
              <div class="error-message"></div>
              <div class="sent-message">Your subscription request has been sent. Thank you!</div>
            </form>
          </div>

        </div>
      </div>
    </div>

    <div class="copyright">
      <div class="container text-center">
        <p>© <span>Copyright</span> <strong class="px-1">2025</strong> <strong class="px-1 sitename">DevTechAI.Org</strong> <span>All Rights Reserved</span></p>
        <div class="credits">
          Designed by <a href="https://devtechai.org/">DevTechAI Team</a>
        </div>
      </div>
    </div>

  </footer>

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Preloader -->
  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="../assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/vendor/php-email-form/validate.js"></script>
  <script src="../assets/vendor/aos/aos.js"></script>
  <script src="../assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="../assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="../assets/vendor/imagesloaded/imagesloaded.pkgd.min.js"></script>
  <script src="../assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="../assets/vendor/purecounter/purecounter_vanilla.js"></script>

  <!-- Main JS File -->
  <script src="../assets/js/main.js"></script>

</body>

</html>"""

    os.makedirs(os.path.dirname(f"solutions/{filename}"), exist_ok=True)
    with open(f"solutions/{filename}", "w") as f:
        f.write(html_content)
    print(f"Generated: solutions/{filename}")

# Solutions Data
solutions = [
    {
        "title": "AI Solutions",
        "description": "Comprehensive AI integration and modernization services",
        "filename": "ai-solutions",
        "icon": "cpu",
        "content": """
              <p>
                DevTechAI provides comprehensive AI solutions that transform businesses through intelligent automation, advanced analytics, and seamless integration with leading AI platforms.
              </p>
              <h3>Our AI Capabilities</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>Multi-Model AI Integration:</strong> Seamlessly integrate OpenAI GPT-4, Anthropic Claude, Google Gemini, and Azure OpenAI into your applications</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Intelligent Automation:</strong> Automate complex business processes with AI-powered decision-making and workflow optimization</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Advanced Analytics:</strong> Leverage machine learning models for predictive analytics, pattern recognition, and data-driven insights</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Natural Language Processing:</strong> Implement conversational AI, chatbots, and intelligent content generation systems</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Computer Vision:</strong> Image recognition, object detection, and visual analytics solutions</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Custom AI Models:</strong> Develop and deploy tailored machine learning models for your specific business needs</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                Our AI solutions help businesses increase efficiency by up to 60%, reduce operational costs by 40%, and accelerate innovation through intelligent automation and data-driven decision-making.
              </p>
              <h3>Use Cases</h3>
              <ul>
                <li>Customer support automation with intelligent chatbots</li>
                <li>Content generation and personalization at scale</li>
                <li>Predictive maintenance and anomaly detection</li>
                <li>Intelligent document processing and extraction</li>
                <li>Real-time recommendation engines</li>
                <li>Fraud detection and security analytics</li>
              </ul>
            """
    },
    {
        "title": "N8N Integration",
        "description": "Powerful workflow automation with N8N platform",
        "filename": "n8n-integration",
        "icon": "diagram-3",
        "content": """
              <p>
                N8N is a powerful open-source workflow automation tool that enables you to connect different services and automate complex business processes without writing code.
              </p>
              <h3>N8N Integration Services</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>Workflow Design & Development:</strong> Create custom workflows using N8N's visual interface to automate your business processes</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>500+ Pre-built Integrations:</strong> Connect with popular services like Slack, Google Workspace, Salesforce, and more</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Custom Node Development:</strong> Build custom nodes for specialized integrations and business logic</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Webhook Management:</strong> Set up and manage webhooks for real-time event-driven workflows</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Error Handling & Retry Logic:</strong> Implement robust error handling and automatic retry mechanisms</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Workflow Monitoring:</strong> Monitor workflow execution, performance, and troubleshoot issues</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                N8N integration helps automate repetitive tasks, reduce manual work by up to 80%, improve process efficiency, and enable seamless data flow between different systems and services.
              </p>
              <h3>Common Use Cases</h3>
              <ul>
                <li>Automated lead management and CRM updates</li>
                <li>Data synchronization between multiple platforms</li>
                <li>Automated report generation and distribution</li>
                <li>Real-time notifications and alerts</li>
                <li>E-commerce order processing automation</li>
                <li>Social media content scheduling and posting</li>
              </ul>
            """
    },
    {
        "title": "Zapier Automation",
        "description": "Streamline workflows with Zapier automation platform",
        "filename": "zapier-automation",
        "icon": "lightning",
        "content": """
              <p>
                Zapier is a leading no-code automation platform that connects your favorite apps and automates workflows, enabling you to work more efficiently and focus on what matters most.
              </p>
              <h3>Zapier Automation Services</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>Zap Creation & Configuration:</strong> Design and set up automated workflows (Zaps) between your applications</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>6,000+ App Integrations:</strong> Connect with thousands of popular apps including Gmail, Slack, Trello, HubSpot, and more</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Multi-Step Workflows:</strong> Create complex automation workflows with conditional logic and data transformations</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Custom Integrations:</strong> Build custom Zapier integrations for your proprietary systems using Zapier CLI</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Workflow Optimization:</strong> Optimize existing Zaps for better performance and reliability</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Team Collaboration:</strong> Set up shared Zaps and manage team access and permissions</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                Zapier automation eliminates manual data entry, reduces errors, saves time, and enables seamless integration between your business tools, resulting in increased productivity and efficiency.
              </p>
              <h3>Common Use Cases</h3>
              <ul>
                <li>Lead capture and CRM automation</li>
                <li>Email marketing campaign automation</li>
                <li>Invoice and payment processing</li>
                <li>Social media content management</li>
                <li>Customer support ticket routing</li>
                <li>Data backup and synchronization</li>
              </ul>
            """
    },
    {
        "title": "Custom Workflows",
        "description": "Tailored workflow automation solutions for your business",
        "filename": "custom-workflows",
        "icon": "sliders",
        "content": """
              <p>
                Every business has unique processes and requirements. Our custom workflow solutions are designed specifically for your business needs, ensuring optimal efficiency and seamless integration with your existing systems.
              </p>
              <h3>Custom Workflow Services</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>Process Analysis & Design:</strong> Analyze your business processes and design optimized workflows tailored to your needs</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Workflow Development:</strong> Build custom automation workflows using various platforms and technologies</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Integration Development:</strong> Create custom integrations between your systems and third-party services</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>API Development:</strong> Develop custom APIs to enable workflow automation and system communication</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Workflow Testing & Optimization:</strong> Test workflows thoroughly and optimize for performance and reliability</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Documentation & Training:</strong> Provide comprehensive documentation and training for your team</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                Custom workflows are designed specifically for your business, ensuring maximum efficiency, seamless integration, and scalability. They eliminate bottlenecks, reduce manual work, and improve overall productivity.
              </p>
              <h3>Common Use Cases</h3>
              <ul>
                <li>Industry-specific process automation</li>
                <li>Legacy system integration and modernization</li>
                <li>Complex multi-system workflows</li>
                <li>Compliance and regulatory automation</li>
                <li>Custom reporting and analytics workflows</li>
                <li>Specialized business process automation</li>
              </ul>
            """
    },
    {
        "title": "API Integrations",
        "description": "Seamless API integration services for connecting your systems",
        "filename": "api-integrations",
        "icon": "plug",
        "content": """
              <p>
                API integrations enable seamless communication between different systems, services, and applications. Our API integration services help you connect your business tools and automate data flow.
              </p>
              <h3>API Integration Services</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>RESTful API Integration:</strong> Integrate with REST APIs for modern web services and applications</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>GraphQL Integration:</strong> Connect with GraphQL APIs for efficient data fetching and manipulation</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>SOAP API Integration:</strong> Integrate with legacy SOAP-based web services</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Authentication & Security:</strong> Implement secure authentication mechanisms (OAuth, API keys, JWT) for API access</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Error Handling & Retry Logic:</strong> Implement robust error handling and automatic retry mechanisms for reliable API communication</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>API Gateway Setup:</strong> Set up and configure API gateways for centralized API management</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                API integrations enable real-time data synchronization, automate business processes, improve system interoperability, and create a unified ecosystem of connected applications and services.
              </p>
              <h3>Common Use Cases</h3>
              <ul>
                <li>Third-party service integration (payment gateways, shipping, etc.)</li>
                <li>CRM and marketing automation platform connections</li>
                <li>E-commerce platform integrations</li>
                <li>Cloud service API connections</li>
                <li>Database and data warehouse integrations</li>
                <li>Social media and communication platform APIs</li>
              </ul>
            """
    },
    {
        "title": "Webhook Management",
        "description": "Real-time event-driven automation with webhook solutions",
        "filename": "webhook-management",
        "icon": "broadcast",
        "content": """
              <p>
                Webhooks enable real-time, event-driven communication between systems. Our webhook management services help you set up, manage, and monitor webhooks for seamless automation and integration.
              </p>
              <h3>Webhook Management Services</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>Webhook Setup & Configuration:</strong> Set up webhooks for various services and configure event triggers</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Webhook Security:</strong> Implement secure webhook endpoints with signature verification and authentication</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Webhook Monitoring:</strong> Monitor webhook delivery, success rates, and troubleshoot issues</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Webhook Retry Logic:</strong> Implement automatic retry mechanisms for failed webhook deliveries</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Webhook Transformation:</strong> Transform webhook payloads to match your system requirements</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Webhook Testing & Debugging:</strong> Test webhooks in development and production environments</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                Webhook management enables real-time event processing, reduces polling overhead, improves system responsiveness, and enables instant notifications and automated actions based on events.
              </p>
              <h3>Common Use Cases</h3>
              <ul>
                <li>Real-time order processing and fulfillment</li>
                <li>Instant notification systems</li>
                <li>Event-driven workflow automation</li>
                <li>Payment and transaction processing</li>
                <li>Git repository webhook integrations</li>
                <li>Cloud service event notifications</li>
              </ul>
            """
    },
    {
        "title": "Cloud Services",
        "description": "Comprehensive cloud solutions across AWS, GCP, Azure, and OCI",
        "filename": "cloud-services",
        "icon": "cloud",
        "content": """
              <p>
                DevTechAI provides comprehensive cloud services across major cloud providers, enabling you to leverage the best cloud infrastructure for your business needs with a cloud-agnostic approach.
              </p>
              <h3>Cloud Services Offered</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>AWS Services:</strong> Amazon Web Services deployment, migration, and management including EC2, S3, Lambda, RDS, and more</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Google Cloud Platform:</strong> GCP services including Compute Engine, Cloud Storage, BigQuery, Cloud Functions, and AI/ML services</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Microsoft Azure:</strong> Azure services including Virtual Machines, Blob Storage, Azure Functions, and Azure AI services</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Oracle Cloud Infrastructure:</strong> OCI services including Compute, Object Storage, Autonomous Database, and AI services</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Multi-Cloud Strategy:</strong> Design and implement multi-cloud architectures for redundancy and optimization</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Cloud Migration:</strong> Migrate existing applications and infrastructure to the cloud with minimal downtime</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                Cloud services provide scalability, flexibility, cost-efficiency, and global reach. Our cloud-agnostic approach ensures you can leverage the best services from each provider while maintaining flexibility and avoiding vendor lock-in.
              </p>
              <h3>Common Use Cases</h3>
              <ul>
                <li>Application hosting and deployment</li>
                <li>Data storage and backup solutions</li>
                <li>AI/ML model training and deployment</li>
                <li>Database hosting and management</li>
                <li>Content delivery and CDN setup</li>
                <li>Disaster recovery and business continuity</li>
              </ul>
            """
    },
    {
        "title": "Monitoring",
        "description": "Comprehensive monitoring and observability solutions",
        "filename": "monitoring",
        "icon": "activity",
        "content": """
              <p>
                Effective monitoring and observability are crucial for maintaining system health, performance, and reliability. Our monitoring solutions provide real-time insights into your applications and infrastructure.
              </p>
              <h3>Monitoring Services</h3>
              <ul>
                <li><i class="bi bi-check-circle"></i> <span><strong>Application Performance Monitoring:</strong> Monitor application performance, response times, and user experience with tools like New Relic, Datadog, and APM</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Infrastructure Monitoring:</strong> Monitor server health, resource utilization, and infrastructure metrics with Prometheus and Grafana</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Log Management:</strong> Centralized log aggregation, analysis, and search with ELK Stack, Splunk, or cloud-native solutions</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Error Tracking:</strong> Track and analyze application errors with Sentry and similar tools</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Alerting & Notifications:</strong> Set up intelligent alerting systems for proactive issue detection and resolution</span></li>
                <li><i class="bi bi-check-circle"></i> <span><strong>Custom Dashboards:</strong> Create custom monitoring dashboards tailored to your business needs</span></li>
              </ul>
              <h3>Benefits</h3>
              <p>
                Comprehensive monitoring enables proactive issue detection, faster incident response, improved system reliability, better performance optimization, and data-driven decision-making for infrastructure and application improvements.
              </p>
              <h3>Common Use Cases</h3>
              <ul>
                <li>Real-time application performance monitoring</li>
                <li>Infrastructure health and resource monitoring</li>
                <li>Error tracking and debugging</li>
                <li>Business metrics and KPI tracking</li>
                <li>Security event monitoring</li>
                <li>Compliance and audit logging</li>
              </ul>
            """
    }
]

# Create solutions directory
os.makedirs("solutions", exist_ok=True)

# Generate each solution page
for solution in solutions:
    generate_solution_page(
        solution["title"],
        solution["description"],
        solution["content"],
        solution["filename"],
        solution.get("icon", "gear")
    )

print("\n✅ All solution pages generated successfully!")
print(f"📁 Generated {len(solutions)} solution pages in the 'solutions/' directory")

