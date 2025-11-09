#!/usr/bin/env python3
"""
Generate service detail pages for DevTechAI WebApp
"""

services = [
    {
        "filename": "workflow-automation.html",
        "title": "Workflow Automation",
        "description": "Automate complex business processes using N8N, Zapier, and custom workflow solutions tailored to your needs.",
        "short_desc": "Automate complex business processes using N8N, Zapier, and custom workflow solutions.",
        "content": """
            <h3>Intelligent Workflow Automation Platform</h3>
            <p>
              Our Workflow Automation service empowers businesses to streamline operations, reduce manual work, and increase efficiency through intelligent automation. We integrate with leading workflow platforms including N8N, Zapier, Airtable, and custom solutions.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Multi-platform workflow integration (N8N, Zapier, Airtable)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Custom workflow design and implementation</span></li>
              <li><i class="bi bi-check-circle"></i> <span>API integrations and webhook management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Real-time monitoring and error handling</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Scalable automation architecture</span></li>
            </ul>
            <p>
              We design and implement automated workflows that connect your applications, services, and data sources. Our solutions handle complex business logic, error recovery, and scaling requirements.
            </p>
            <h4>Key Features</h4>
            <p>
              <strong>N8N Integration:</strong> Self-hosted or cloud-based workflow automation with visual workflow builder and extensive integrations.
            </p>
            <p>
              <strong>Zapier Automation:</strong> Connect thousands of apps with pre-built integrations and custom zaps for your specific needs.
            </p>
            <p>
              <strong>Custom Workflows:</strong> Tailored automation solutions built specifically for your business processes and requirements.
            </p>
            <p>
              <strong>API & Webhook Management:</strong> Secure API integrations and webhook handling for real-time data synchronization and event-driven automation.
            </p>
        """
    },
    {
        "filename": "cloud-ai-solutions.html",
        "title": "Cloud AI Solutions",
        "description": "Deploy and manage AI-powered applications across AWS, GCP, OCI, and Azure with our cloud-agnostic platform.",
        "short_desc": "Deploy and manage AI-powered applications across AWS, GCP, OCI, and Azure.",
        "content": """
            <h3>Multi-Cloud AI Deployment Platform</h3>
            <p>
              Our Cloud AI Solutions service provides a cloud-agnostic platform for deploying, managing, and scaling AI-powered applications across major cloud providers. We support AWS, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI), and Microsoft Azure.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Multi-cloud deployment and management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cloud-agnostic architecture design</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Auto-scaling and load balancing</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cost optimization and resource management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Disaster recovery and high availability</span></li>
            </ul>
            <p>
              We help businesses leverage the best features from each cloud provider while maintaining flexibility and avoiding vendor lock-in. Our platform ensures consistent deployment, monitoring, and management across all cloud environments.
            </p>
            <h4>Supported Cloud Platforms</h4>
            <p>
              <strong>AWS:</strong> Amazon Web Services integration with EC2, Lambda, SageMaker, and other AI services.
            </p>
            <p>
              <strong>Google Cloud Platform:</strong> GCP services including Compute Engine, Cloud Functions, Vertex AI, and BigQuery.
            </p>
            <p>
              <strong>Oracle Cloud Infrastructure:</strong> OCI services with autonomous databases, compute instances, and AI services.
            </p>
            <p>
              <strong>Microsoft Azure:</strong> Azure services including Virtual Machines, Functions, Azure OpenAI, and Cognitive Services.
            </p>
        """
    },
    {
        "filename": "monitoring-analytics.html",
        "title": "Monitoring & Analytics",
        "description": "Comprehensive monitoring with Prometheus, Grafana, and custom analytics dashboards for real-time insights.",
        "short_desc": "Comprehensive monitoring with Prometheus, Grafana, and custom analytics dashboards.",
        "content": """
            <h3>Advanced Monitoring and Analytics Platform</h3>
            <p>
              Our Monitoring & Analytics service provides comprehensive observability for your applications, infrastructure, and business metrics. We integrate with leading monitoring tools including Prometheus, Grafana, Datadog, New Relic, and custom solutions.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Real-time application and infrastructure monitoring</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Custom dashboards and visualization</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Alerting and incident management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Performance analytics and optimization</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Log aggregation and analysis</span></li>
            </ul>
            <p>
              We provide end-to-end monitoring solutions that give you complete visibility into your systems. Our dashboards and alerts help you identify issues before they impact users and optimize performance continuously.
            </p>
            <h4>Monitoring Tools</h4>
            <p>
              <strong>Prometheus & Grafana:</strong> Open-source monitoring stack with powerful querying and visualization capabilities.
            </p>
            <p>
              <strong>Datadog:</strong> Cloud-based monitoring with APM, infrastructure monitoring, and log management.
            </p>
            <p>
              <strong>New Relic:</strong> Application performance monitoring with full-stack observability and AI-powered insights.
            </p>
            <p>
              <strong>Custom Analytics:</strong> Tailored analytics solutions built specifically for your business metrics and KPIs.
            </p>
        """
    },
    {
        "filename": "security-compliance.html",
        "title": "Security & Compliance",
        "description": "Enterprise-grade security with GDPR, CCPA, HIPAA compliance and advanced threat detection systems.",
        "short_desc": "Enterprise-grade security with GDPR, CCPA, HIPAA compliance.",
        "content": """
            <h3>Enterprise Security and Compliance Solutions</h3>
            <p>
              Our Security & Compliance service ensures your applications meet the highest security standards and regulatory requirements. We provide comprehensive security solutions including GDPR, CCPA, HIPAA compliance, and advanced threat detection.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Regulatory compliance (GDPR, CCPA, HIPAA)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Advanced threat detection and prevention</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Data encryption and privacy protection</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Security audits and penetration testing</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Identity and access management (IAM)</span></li>
            </ul>
            <p>
              We help businesses protect their data, applications, and infrastructure from threats while ensuring compliance with industry regulations. Our security solutions are designed to scale with your business and adapt to evolving threats.
            </p>
            <h4>Compliance Standards</h4>
            <p>
              <strong>GDPR:</strong> General Data Protection Regulation compliance for EU data protection requirements.
            </p>
            <p>
              <strong>CCPA:</strong> California Consumer Privacy Act compliance for California residents' data rights.
            </p>
            <p>
              <strong>HIPAA:</strong> Health Insurance Portability and Accountability Act compliance for healthcare data.
            </p>
            <p>
              <strong>Security Services:</strong> Threat detection, vulnerability scanning, security monitoring, and incident response.
            </p>
        """
    },
    {
        "filename": "api-development.html",
        "title": "API Development",
        "description": "Build robust APIs with comprehensive documentation, authentication, and integration capabilities.",
        "short_desc": "Build robust APIs with comprehensive documentation and authentication.",
        "content": """
            <h3>Professional API Development Services</h3>
            <p>
              Our API Development service helps businesses build robust, scalable, and well-documented APIs that enable seamless integration with third-party services and internal systems. We follow industry best practices for API design, security, and documentation.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>RESTful and GraphQL API design</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Comprehensive API documentation (OpenAPI/Swagger)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Authentication and authorization (OAuth, JWT)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Rate limiting and API versioning</span></li>
              <li><i class="bi bi-check-circle"></i> <span>API testing and monitoring</span></li>
            </ul>
            <p>
              We design and develop APIs that are secure, performant, and easy to integrate. Our APIs are built with scalability in mind and include comprehensive documentation, testing, and monitoring capabilities.
            </p>
            <h4>API Features</h4>
            <p>
              <strong>RESTful APIs:</strong> Standard REST APIs following best practices for resource design and HTTP methods.
            </p>
            <p>
              <strong>GraphQL APIs:</strong> Flexible GraphQL APIs for efficient data fetching and reduced over-fetching.
            </p>
            <p>
              <strong>API Documentation:</strong> Comprehensive documentation using OpenAPI/Swagger with interactive testing capabilities.
            </p>
            <p>
              <strong>Security:</strong> OAuth 2.0, JWT authentication, API keys, and role-based access control (RBAC).
            </p>
        """
    },
    {
        "filename": "ai-app-modernization.html",
        "title": "AI-Powered App Modernization",
        "description": "FullStack Apps modernization with GenAI, AgenticAI multi-model features for enhanced user experiences.",
        "short_desc": "FullStack Apps modernization with GenAI and AgenticAI features.",
        "content": """
            <h3>AI-Powered Application Modernization</h3>
            <p>
              Our AI-Powered App Modernization service transforms legacy applications into modern, intelligent solutions using Generative AI, Agentic AI, and multi-model capabilities. We modernize your applications while enhancing them with cutting-edge AI features.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Legacy application modernization</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Generative AI integration (GenAI)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Agentic AI capabilities</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Multi-model AI architecture</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Enhanced user experience with AI</span></li>
            </ul>
            <p>
              We help businesses modernize their applications by integrating AI capabilities that enhance user experiences, automate processes, and provide intelligent insights. Our modernization approach preserves existing functionality while adding powerful AI features.
            </p>
            <h4>Modernization Features</h4>
            <p>
              <strong>Generative AI:</strong> Integration of GenAI models for content generation, code assistance, and creative applications.
            </p>
            <p>
              <strong>Agentic AI:</strong> Autonomous AI agents that can perform tasks, make decisions, and interact with systems independently.
            </p>
            <p>
              <strong>Multi-Model Architecture:</strong> Support for multiple AI models working together to provide comprehensive capabilities.
            </p>
            <p>
              <strong>User Experience:</strong> AI-powered features that enhance usability, personalization, and user engagement.
            </p>
        """
    },
    {
        "filename": "cloud-saas-development.html",
        "title": "Cloud SaaS Development",
        "description": "Build scalable Software-as-a-Service applications with cloud-native architecture and multi-tenant capabilities.",
        "short_desc": "Build scalable SaaS applications with cloud-native architecture.",
        "content": """
            <h3>Cloud-Native SaaS Development</h3>
            <p>
              Our Cloud SaaS Development service helps businesses build scalable, multi-tenant Software-as-a-Service applications using cloud-native architecture. We design and develop SaaS solutions that can scale from startup to enterprise level.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Multi-tenant architecture design</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cloud-native development (microservices, containers)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Scalable infrastructure and auto-scaling</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Subscription and billing management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>API-first architecture</span></li>
            </ul>
            <p>
              We build SaaS applications that are designed for scale, security, and performance. Our solutions include multi-tenancy, subscription management, and cloud-native architecture that can grow with your business.
            </p>
            <h4>SaaS Features</h4>
            <p>
              <strong>Multi-Tenancy:</strong> Secure multi-tenant architecture with data isolation and tenant management.
            </p>
              <strong>Cloud-Native:</strong> Microservices architecture, containerization, and orchestration with Kubernetes.
            </p>
            <p>
              <strong>Scalability:</strong> Auto-scaling infrastructure that adapts to demand and ensures optimal performance.
            </p>
            <p>
              <strong>Subscription Management:</strong> Complete billing, subscription, and payment processing integration.
            </p>
        """
    },
    {
        "filename": "fullstack-product-development.html",
        "title": "AI Powered FullStack Product Development",
        "description": "End-to-end FullStack SaaS product development with integrated AI capabilities, cloud infrastructure, and scalable architecture.",
        "short_desc": "End-to-end FullStack SaaS product development with AI capabilities.",
        "content": """
            <h3>End-to-End FullStack Product Development</h3>
            <p>
              Our AI Powered FullStack Product Development service provides complete product development from concept to deployment. We build full-stack SaaS products with integrated AI capabilities, cloud infrastructure, and scalable architecture.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Full-stack development (frontend, backend, database)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>AI integration and capabilities</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cloud infrastructure and deployment</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Scalable architecture design</span></li>
              <li><i class="bi bi-check-circle"></i> <span>DevOps and CI/CD pipeline</span></li>
            </ul>
            <p>
              We provide end-to-end product development services that take your idea from concept to production. Our full-stack solutions include everything needed for a successful SaaS product: frontend, backend, database, AI integration, cloud infrastructure, and DevOps.
            </p>
            <h4>Development Stack</h4>
            <p>
              <strong>Frontend:</strong> Modern web and mobile applications with responsive design and excellent UX.
            </p>
            <p>
              <strong>Backend:</strong> Scalable backend services with microservices architecture and API design.
            </p>
            <p>
              <strong>AI Integration:</strong> Seamless integration of AI capabilities throughout the product.
            </p>
            <p>
              <strong>Cloud Infrastructure:</strong> Deploy on AWS, GCP, Azure, or OCI with auto-scaling and high availability.
            </p>
        """
    },
    {
        "filename": "ar-vr-solutions.html",
        "title": "AR/VR Solutions",
        "description": "Immersive Augmented and Virtual Reality experiences with AI-powered interactions and cloud-based rendering capabilities.",
        "short_desc": "Immersive AR/VR experiences with AI-powered interactions.",
        "content": """
            <h3>Immersive AR/VR Solutions</h3>
            <p>
              Our AR/VR Solutions service creates immersive Augmented and Virtual Reality experiences enhanced with AI-powered interactions and cloud-based rendering. We develop AR/VR applications for various industries including training, entertainment, retail, and healthcare.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>AR/VR application development</span></li>
              <li><i class="bi bi-check-circle"></i> <span>AI-powered interactions and object recognition</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cloud-based rendering and processing</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cross-platform compatibility</span></li>
              <li><i class="bi bi-check-circle"></i> <span>3D modeling and asset creation</span></li>
            </ul>
            <p>
              We create immersive AR/VR experiences that combine cutting-edge technology with practical applications. Our solutions leverage AI for intelligent interactions, object recognition, and natural language processing within virtual environments.
            </p>
            <h4>AR/VR Capabilities</h4>
            <p>
              <strong>Augmented Reality:</strong> AR applications for mobile devices, smart glasses, and enterprise solutions.
            </p>
            <p>
              <strong>Virtual Reality:</strong> VR experiences for training, simulation, entertainment, and virtual collaboration.
            </p>
            <p>
              <strong>AI Integration:</strong> AI-powered object recognition, natural language processing, and intelligent interactions.
            </p>
            <p>
              <strong>Cloud Rendering:</strong> Offload heavy rendering tasks to the cloud for better performance on devices.
            </p>
        """
    },
    {
        "filename": "blockchain-solutions.html",
        "title": "Blockchain Solutions",
        "description": "Decentralized applications, smart contracts, and blockchain integration with AI-powered analytics and cloud infrastructure.",
        "short_desc": "Decentralized applications and smart contracts with AI analytics.",
        "content": """
            <h3>Blockchain and Decentralized Solutions</h3>
            <p>
              Our Blockchain Solutions service helps businesses leverage blockchain technology for decentralized applications, smart contracts, and secure transactions. We combine blockchain with AI-powered analytics and cloud infrastructure for comprehensive solutions.
            </p>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Decentralized application (DApp) development</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Smart contract development and auditing</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Blockchain integration and APIs</span></li>
              <li><i class="bi bi-check-circle"></i> <span>AI-powered blockchain analytics</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cloud infrastructure for blockchain nodes</span></li>
            </ul>
            <p>
              We develop blockchain solutions that are secure, scalable, and integrated with your existing systems. Our services include DApp development, smart contracts, and blockchain analytics powered by AI.
            </p>
            <h4>Blockchain Services</h4>
            <p>
              <strong>DApp Development:</strong> Decentralized applications built on Ethereum, Polygon, or other blockchain networks.
            </p>
            <p>
              <strong>Smart Contracts:</strong> Secure smart contract development, testing, and auditing for various use cases.
            </p>
            <p>
              <strong>Blockchain Integration:</strong> APIs and integration services to connect blockchain with traditional systems.
            </p>
            <p>
              <strong>AI Analytics:</strong> AI-powered analytics for blockchain data, transaction patterns, and insights.
            </p>
        """
    },
    {
        "filename": "mobile-development.html",
        "title": "Android & iOS Development",
        "description": "Native and cross-platform mobile app development with AI integration, cloud connectivity, and modern UI/UX design.",
        "short_desc": "Native and cross-platform mobile app development with AI integration.",
        "content": """
            <h3>Mobile Application Development</h3>
            <p>
              Our Android & iOS Development service creates native and cross-platform mobile applications with AI integration, cloud connectivity, and modern UI/UX design. We develop mobile apps that provide exceptional user experiences across all devices.
            </p>
            <ul>
              <i class="bi bi-check-circle"></i> <span>Native iOS and Android development</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cross-platform development (React Native, Flutter)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>AI integration in mobile apps</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cloud connectivity and synchronization</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Modern UI/UX design</span></li>
            </ul>
            <p>
              We develop mobile applications that leverage the latest technologies including AI, cloud services, and modern design principles. Our apps are performant, secure, and provide excellent user experiences.
            </p>
            <h4>Mobile Development</h4>
            <p>
              <strong>Native Development:</strong> iOS apps with Swift/SwiftUI and Android apps with Kotlin/Jetpack Compose.
            </p>
            <p>
              <strong>Cross-Platform:</strong> React Native and Flutter apps for code sharing across platforms.
            </p>
            <p>
              <strong>AI Integration:</strong> On-device and cloud-based AI features for intelligent mobile experiences.
            </p>
            <p>
              <strong>Cloud Services:</strong> Integration with cloud backends, real-time synchronization, and offline capabilities.
            </p>
        """
    }
]

template = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{title} - DevTechAI</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="DevTechAI, {title}, AI solutions, cloud services">

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
          <li><a href="../index.html#services" class="active">Services</a></li>
          <li><a href="../index.html#portfolio">Portfolio</a></li>
          <li><a href="../index.html#team">Team</a></li>
          <li><a href="../index.html#contact">Contact</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>

      <a class="btn-getstarted" href="../index.html#contact">Get Started</a>

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
              <p class="mb-0">{short_desc}</p>
            </div>
          </div>
        </div>
      </div>
      <nav class="breadcrumbs">
        <div class="container">
          <ol>
            <li><a href="../index.html">Home</a></li>
            <li><a href="../index.html#services">Services</a></li>
            <li class="current">{title}</li>
          </ol>
        </div>
      </nav>
    </div><!-- End Page Title -->

    <!-- Service Details Section -->
    <section id="service-details" class="service-details section">

      <div class="container">

        <div class="row gy-5">

          <div class="col-lg-4" data-aos="fade-up" data-aos-delay="100">

            <div class="service-box">
              <h4>Our Services</h4>
              <div class="services-list">
                <a href="ai-modernization.html"><i class="bi bi-arrow-right-circle"></i><span>AI Modernization</span></a>
                <a href="workflow-automation.html"><i class="bi bi-arrow-right-circle"></i><span>Workflow Automation</span></a>
                <a href="cloud-ai-solutions.html"><i class="bi bi-arrow-right-circle"></i><span>Cloud AI Solutions</span></a>
                <a href="monitoring-analytics.html"><i class="bi bi-arrow-right-circle"></i><span>Monitoring & Analytics</span></a>
                <a href="security-compliance.html"><i class="bi bi-arrow-right-circle"></i><span>Security & Compliance</span></a>
                <a href="api-development.html"><i class="bi bi-arrow-right-circle"></i><span>API Development</span></a>
                <a href="ai-app-modernization.html"><i class="bi bi-arrow-right-circle"></i><span>AI-Powered App Modernization</span></a>
                <a href="cloud-saas-development.html"><i class="bi bi-arrow-right-circle"></i><span>Cloud SaaS Development</span></a>
                <a href="fullstack-product-development.html"><i class="bi bi-arrow-right-circle"></i><span>AI Powered FullStack Development</span></a>
                <a href="ar-vr-solutions.html"><i class="bi bi-arrow-right-circle"></i><span>AR/VR Solutions</span></a>
                <a href="blockchain-solutions.html"><i class="bi bi-arrow-right-circle"></i><span>Blockchain Solutions</span></a>
                <a href="mobile-development.html"><i class="bi bi-arrow-right-circle"></i><span>Android & iOS Development</span></a>
              </div>
            </div>

            <div class="help-box d-flex flex-column justify-content-center align-items-center">
              <i class="bi bi-headset help-icon"></i>
              <h4>Have a Question?</h4>
              <p class="d-flex align-items-center mt-2 mb-0"><i class="bi bi-telephone me-2"></i> <span>+1 (555) 123-4567</span></p>
              <p class="d-flex align-items-center mt-1 mb-0"><i class="bi bi-envelope me-2"></i> <a href="mailto:info@devtechai.org">info@devtechai.org</a></p>
            </div>

          </div>

          <div class="col-lg-8 ps-lg-5" data-aos="fade-up" data-aos-delay="200">
            <img src="../assets/img/services.jpg" alt="{title}" class="img-fluid services-img">
            {content}
          </div>

        </div>

      </div>

    </section>

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
              <p>123 AI Innovation Drive</p>
              <p>Tech Valley, CA 94000</p>
              <p class="mt-3"><strong>Phone:</strong> <span>+1 (555) 123-4567</span></p>
              <p><strong>Email:</strong> <span>info@devtechai.org</span></p>
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
              <li><i class="bi bi-chevron-right"></i> <a href="ai-modernization.html"> AI Modernization</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="workflow-automation.html"> Workflow Automation</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="cloud-ai-solutions.html"> Cloud AI Solutions</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="monitoring-analytics.html"> Monitoring & Analytics</a></li>
              <li><i class="bi bi-chevron-right"></i> <a href="security-compliance.html"> Security & Compliance</a></li>
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
        <p>© <span>Copyright</span> <strong class="px-1 sitename">DevTechAI.Org</strong> <span>All Rights Reserved</span></p>
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

if __name__ == "__main__":
    import os
    os.makedirs("services", exist_ok=True)
    
    for service in services:
        filename = f"services/{service['filename']}"
        content = template.format(
            title=service['title'],
            description=service['description'],
            short_desc=service['short_desc'],
            content=service['content']
        )
        
        # Update active link in services list
        active_class = ' class="active"' if service['filename'] == 'ai-modernization.html' else ''
        content = content.replace(
            f'<a href="{service["filename"]}"><i class="bi bi-arrow-right-circle"></i><span>{service["title"]}</span></a>',
            f'<a href="{service["filename"]}"{active_class}><i class="bi bi-arrow-right-circle"></i><span>{service["title"]}</span></a>'
        )
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"Generated: {filename}")

