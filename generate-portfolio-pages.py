#!/usr/bin/env python3
"""
Generate portfolio detail pages for DevTechAI WebApp
"""

portfolios = [
    {
        "filename": "ai-chat-platform.html",
        "title": "AI Chat Platform",
        "subtitle": "Multi-model AI integration",
        "category": "AI Solutions",
        "image": "masonry-portfolio-1.jpg",
        "content": """
            <h3>Revolutionary Multi-Model AI Chat Platform</h3>
            <p>
              We developed a cutting-edge AI chat platform that seamlessly integrates multiple AI models including OpenAI GPT-4, Anthropic Claude, Google Gemini, and Azure OpenAI. This platform provides businesses with a unified interface to leverage the best capabilities from each AI provider.
            </p>
            <p>
              The platform features intelligent model routing, cost optimization, and real-time performance monitoring. It supports conversational AI, code generation, content creation, and advanced reasoning capabilities across all integrated models.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Multi-model AI integration (OpenAI, Anthropic, Google, Azure)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Intelligent model routing and load balancing</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Real-time conversation management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Cost optimization and usage analytics</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Enterprise-grade security and compliance</span></li>
            </ul>
            <p>
              The platform has been successfully deployed for enterprise clients, handling millions of conversations monthly with 99.9% uptime and sub-second response times.
            </p>
        """
    },
    {
        "filename": "workflow-engine.html",
        "title": "Workflow Engine",
        "subtitle": "N8N-powered automation",
        "category": "Automation",
        "image": "masonry-portfolio-2.jpg",
        "content": """
            <h3>Enterprise Workflow Automation Engine</h3>
            <p>
              Built on N8N, this workflow automation engine enables businesses to automate complex processes across multiple systems and services. The platform integrates with over 500+ applications and services, providing seamless automation capabilities.
            </p>
            <p>
              The engine features visual workflow builder, error handling, retry mechanisms, and comprehensive logging. It supports webhooks, API integrations, database connections, and custom node development for specialized requirements.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>N8N-based workflow automation platform</span></li>
              <li><i class="bi bi-check-circle"></i> <span>500+ pre-built integrations</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Visual workflow builder with drag-and-drop interface</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Error handling and retry mechanisms</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Real-time monitoring and logging</span></li>
            </ul>
            <p>
              This solution has automated over 10,000 workflows for clients, reducing manual work by 80% and improving process efficiency significantly.
            </p>
        """
    },
    {
        "filename": "cloud-migration.html",
        "title": "Cloud Migration",
        "subtitle": "Multi-cloud deployment",
        "category": "Cloud",
        "image": "masonry-portfolio-3.jpg",
        "content": """
            <h3>Multi-Cloud Migration and Deployment Platform</h3>
            <p>
              We developed a comprehensive cloud migration platform that enables seamless deployment across AWS, Google Cloud Platform, Microsoft Azure, and Oracle Cloud Infrastructure. The platform provides cloud-agnostic architecture with automated migration tools.
            </p>
              <p>
              The solution includes infrastructure as code (Terraform), container orchestration (Kubernetes), automated CI/CD pipelines, and multi-cloud monitoring. It ensures zero-downtime migrations and provides rollback capabilities.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Multi-cloud deployment (AWS, GCP, Azure, OCI)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Infrastructure as Code with Terraform</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Kubernetes orchestration</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Automated CI/CD pipelines</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Zero-downtime migration capabilities</span></li>
            </ul>
            <p>
              Successfully migrated 50+ enterprise applications to cloud infrastructure, reducing infrastructure costs by 40% and improving scalability.
            </p>
        """
    },
    {
        "filename": "ai-analytics.html",
        "title": "AI Analytics",
        "subtitle": "Predictive analytics platform",
        "category": "AI Solutions",
        "image": "masonry-portfolio-4.jpg",
        "content": """
            <h3>AI-Powered Predictive Analytics Platform</h3>
            <p>
              This advanced analytics platform leverages machine learning and AI to provide predictive insights, trend analysis, and data-driven recommendations. The platform processes large-scale data in real-time and delivers actionable intelligence.
            </p>
            <p>
              Built with modern data stack including Apache Spark, TensorFlow, and cloud data warehouses, the platform supports various data sources and provides interactive dashboards for visualization.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Real-time predictive analytics</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Machine learning model integration</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Interactive dashboards and visualizations</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Multi-source data integration</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Automated report generation</span></li>
            </ul>
            <p>
              The platform has helped clients improve decision-making accuracy by 65% and identify business opportunities worth millions in revenue.
            </p>
        """
    },
    {
        "filename": "api-gateway.html",
        "title": "API Gateway",
        "subtitle": "Enterprise API management",
        "category": "Automation",
        "image": "masonry-portfolio-5.jpg",
        "content": """
            <h3>Enterprise API Gateway and Management Platform</h3>
            <p>
              A comprehensive API gateway solution that provides centralized API management, security, rate limiting, and analytics. The platform supports REST, GraphQL, and gRPC APIs with unified management interface.
            </p>
            <p>
              Features include OAuth 2.0 authentication, API versioning, request/response transformation, caching, and comprehensive API documentation. The gateway handles millions of API requests daily with high availability.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Unified API management for REST, GraphQL, and gRPC</span></li>
              <li><i class="bi bi-check-circle"></i> <span>OAuth 2.0 and JWT authentication</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Rate limiting and throttling</span></li>
              <li><i class="bi bi-check-circle"></i> <span>API versioning and lifecycle management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Comprehensive analytics and monitoring</span></li>
            </ul>
            <p>
              The gateway manages 500+ APIs for enterprise clients, processing over 100 million requests monthly with 99.99% uptime.
            </p>
        """
    },
    {
        "filename": "monitoring-dashboard.html",
        "title": "Monitoring Dashboard",
        "subtitle": "Real-time system monitoring",
        "category": "Cloud",
        "image": "masonry-portfolio-6.jpg",
        "content": """
            <h3>Real-Time System Monitoring and Observability Dashboard</h3>
            <p>
              A comprehensive monitoring solution that provides real-time visibility into application performance, infrastructure metrics, and business KPIs. The dashboard integrates with Prometheus, Grafana, Datadog, and custom monitoring tools.
            </p>
            <p>
              The platform features customizable dashboards, alerting rules, log aggregation, distributed tracing, and AI-powered anomaly detection. It supports multiple data sources and provides unified view across all systems.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Real-time metrics and performance monitoring</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Customizable dashboards and visualizations</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Intelligent alerting and incident management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Log aggregation and analysis</span></li>
              <li><i class="bi bi-check-circle"></i> <span>AI-powered anomaly detection</span></li>
            </ul>
            <p>
              The monitoring platform has helped clients reduce mean time to resolution (MTTR) by 70% and prevent 95% of potential incidents through proactive alerting.
            </p>
        """
    },
    {
        "filename": "ml-pipeline.html",
        "title": "ML Pipeline",
        "subtitle": "Machine learning automation",
        "category": "AI Solutions",
        "image": "masonry-portfolio-7.jpg",
        "content": """
            <h3>Automated Machine Learning Pipeline Platform</h3>
            <p>
              An end-to-end ML pipeline platform that automates the entire machine learning lifecycle from data ingestion to model deployment. The platform supports feature engineering, model training, hyperparameter tuning, and automated deployment.
            </p>
            <p>
              Built with MLOps best practices, the platform includes version control for models, experiment tracking, model registry, and automated retraining pipelines. It supports various ML frameworks including TensorFlow, PyTorch, and scikit-learn.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Automated ML lifecycle management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Feature engineering and data preprocessing</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Model training and hyperparameter tuning</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Model versioning and registry</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Automated model deployment and monitoring</span></li>
            </ul>
            <p>
              The platform has enabled clients to deploy 200+ ML models into production, reducing model development time by 60% and improving model accuracy through automated optimization.
            </p>
        """
    },
    {
        "filename": "data-pipeline.html",
        "title": "Data Pipeline",
        "subtitle": "Automated data processing",
        "category": "Automation",
        "image": "masonry-portfolio-8.jpg",
        "content": """
            <h3>Enterprise Data Pipeline and ETL Platform</h3>
            <p>
              A scalable data pipeline platform that automates data extraction, transformation, and loading (ETL) processes. The platform handles batch and real-time data processing with support for various data sources and destinations.
            </p>
            <p>
              Built with Apache Airflow, Apache Kafka, and cloud data services, the platform provides data quality checks, error handling, data lineage tracking, and automated scheduling. It processes terabytes of data daily.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Automated ETL/ELT pipelines</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Batch and real-time data processing</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Data quality validation and monitoring</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Data lineage and cataloging</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Scalable architecture for large datasets</span></li>
            </ul>
            <p>
              The platform processes over 50TB of data daily for enterprise clients, reducing data processing time by 75% and ensuring 99.9% data quality accuracy.
            </p>
        """
    },
    {
        "filename": "security-framework.html",
        "title": "Security Framework",
        "subtitle": "Enterprise security solution",
        "category": "Cloud",
        "image": "masonry-portfolio-9.jpg",
        "content": """
            <h3>Enterprise Security and Compliance Framework</h3>
            <p>
              A comprehensive security framework that provides end-to-end security solutions including identity and access management, threat detection, vulnerability scanning, and compliance management. The framework supports GDPR, CCPA, HIPAA, and SOC 2 compliance.
            </p>
            <p>
              The framework includes security monitoring, incident response automation, encryption at rest and in transit, and security policy enforcement. It integrates with leading security tools and provides unified security dashboard.
            </p>
            <h4>Key Features</h4>
            <ul>
              <li><i class="bi bi-check-circle"></i> <span>Identity and Access Management (IAM)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Advanced threat detection and prevention</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Vulnerability scanning and patch management</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Compliance management (GDPR, CCPA, HIPAA, SOC 2)</span></li>
              <li><i class="bi bi-check-circle"></i> <span>Security incident response automation</span></li>
            </ul>
            <p>
              The security framework has helped clients achieve 100% compliance with regulatory requirements and prevented 99.9% of security threats through proactive monitoring and automated response.
            </p>
        """
    }
]

template = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{title} - DevTechAI Portfolio</title>
  <meta name="description" content="{subtitle}">
  <meta name="keywords" content="DevTechAI, {title}, {category}, portfolio">

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

<body class="portfolio-details-page">

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
          <li><a href="../index.html#portfolio" class="active">Portfolio</a></li>
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
              <p class="mb-0">{subtitle}</p>
            </div>
          </div>
        </div>
      </div>
      <nav class="breadcrumbs">
        <div class="container">
          <ol>
            <li><a href="../index.html">Home</a></li>
            <li><a href="../index.html#portfolio">Portfolio</a></li>
            <li class="current">{title}</li>
          </ol>
        </div>
      </nav>
    </div><!-- End Page Title -->

    <!-- Portfolio Details Section -->
    <section id="portfolio-details" class="portfolio-details section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4">

          <div class="col-lg-8">
            <div class="portfolio-details-slider swiper init-swiper">

              <script type="application/json" class="swiper-config">
                {{
                  "loop": true,
                  "speed": 600,
                  "autoplay": {{
                    "delay": 5000
                  }},
                  "slidesPerView": "auto",
                  "pagination": {{
                    "el": ".swiper-pagination",
                    "type": "bullets",
                    "clickable": true
                  }}
                }}
              </script>

              <div class="swiper-wrapper align-items-center">

                <div class="swiper-slide">
                  <img src="../assets/img/masonry-portfolio/{image}" alt="{title}">
                </div>

                <div class="swiper-slide">
                  <img src="../assets/img/masonry-portfolio/{image}" alt="{title}">
                </div>

              </div>
              <div class="swiper-pagination"></div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="portfolio-info" data-aos="fade-up" data-aos-delay="200">
              <h3>Project Information</h3>
              <ul>
                <li><strong>Category</strong>: {category}</li>
                <li><strong>Client</strong>: Enterprise Client</li>
                <li><strong>Project Date</strong>: 2024</li>
              </ul>
            </div>
            <div class="portfolio-description" data-aos="fade-up" data-aos-delay="300">
              <h2>Project Overview</h2>
              {content}
            </div>
          </div>

        </div>

      </div>

    </section><!-- /Portfolio Details Section -->

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

if __name__ == "__main__":
    import os
    os.makedirs("portfolio", exist_ok=True)
    
    for portfolio in portfolios:
        filename = f"portfolio/{portfolio['filename']}"
        content = template.format(
            title=portfolio['title'],
            subtitle=portfolio['subtitle'],
            category=portfolio['category'],
            image=portfolio['image'],
            content=portfolio['content']
        )
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"Generated: {filename}")

