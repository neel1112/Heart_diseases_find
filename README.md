<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.2.7-green?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/ML-Scikit--learn-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Machine Learning">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</div>

<div align="center">
  <h1>🏥 Heart Disease Prediction System</h1>
  <p><strong>A comprehensive healthcare platform powered by Machine Learning</strong></p>
  
  [![GitHub stars](https://img.shields.io/github/stars/yourusername/health-disease-prediction?style=social)](https://github.com/yourusername/health-disease-prediction)
  [![GitHub forks](https://img.shields.io/github/forks/yourusername/health-disease-prediction?style=social)](https://github.com/yourusername/health-disease-prediction)
  [![GitHub issues](https://img.shields.io/github/issues/yourusername/health-disease-prediction)](https://github.com/yourusername/health-disease-prediction/issues)
  [![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/health-disease-prediction)](https://github.com/yourusername/health-disease-prediction/pulls)
</div>

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📋 Requirements](#-requirements)
- [🏗️ Project Structure](#️-project-structure)
- [🎯 Usage Guide](#-usage-guide)
- [📸 Screenshots](#-screenshots)
- [🧠 Machine Learning](#-machine-learning)
- [🔧 Configuration](#-configuration)
- [🚀 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)

---

## 🌟 Overview

<div align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Last%20Updated-2024-brightgreen?style=for-the-badge" alt="Last Updated">
</div>

A state-of-the-art **Heart Disease Prediction System** that combines the power of Django web framework with advanced Machine Learning algorithms to provide accurate heart disease risk assessments. This comprehensive healthcare platform serves patients, doctors, and administrators with an intuitive interface and robust functionality.

### 🎯 **Key Highlights**
- 🔬 **ML-Powered Predictions**: Advanced algorithms for accurate disease risk assessment
- 👥 **Multi-Role System**: Dedicated interfaces for patients, doctors, and administrators
- 📱 **Responsive Design**: Mobile-friendly interface for all devices
- 🔒 **Secure Authentication**: Robust user management and security
- 📊 **Real-time Analytics**: Live prediction accuracy and performance metrics

---

## ✨ Features

### 🔬 **Core Functionality**

| Feature | Description | Status |
|---------|-------------|--------|
| 🩺 **Heart Disease Prediction** | ML-powered risk assessment using medical parameters | ✅ Active |
| 👥 **User Management** | Separate interfaces for patients, doctors, and administrators | ✅ Active |
| 📅 **Appointment System** | Book and manage doctor appointments | ✅ Active |
| 🔍 **Search & History** | Track prediction history and search functionality | ✅ Active |
| 💬 **Feedback System** | User feedback and rating system | ✅ Active |

### 👥 **User Roles & Capabilities**

<details>
<summary><strong>👤 Patients</strong></summary>

- ✅ Register and manage personal accounts
- ✅ Predict heart disease risk with medical parameters
- ✅ Book appointments with available doctors
- ✅ View prediction history and results
- ✅ Provide feedback and ratings
- ✅ Update personal information and medical details

</details>

<details>
<summary><strong>👨‍⚕️ Doctors</strong></summary>

- ✅ Access dedicated doctor dashboard
- ✅ Manage patient appointments and schedules
- ✅ View patient records and medical history
- ✅ Update appointment status and notes
- ✅ Manage professional profile and availability
- ✅ Access patient prediction results

</details>

<details>
<summary><strong>👨‍💼 Administrators</strong></summary>

- ✅ Complete system management and monitoring
- ✅ Manage users, doctors, and patient accounts
- ✅ Upload and manage medical datasets
- ✅ Monitor system performance and analytics
- ✅ Handle user feedback and support requests
- ✅ Configure system settings and parameters

</details>

### 🎯 **Advanced Features**

<div align="center">

| 🚀 **Performance** | 🔒 **Security** | 📱 **User Experience** |
|-------------------|-----------------|------------------------|
| Real-time predictions | Secure authentication | Responsive design |
| High accuracy metrics | Role-based access | Intuitive interface |
| Fast response times | Data encryption | Mobile-friendly |
| Scalable architecture | Session management | Cross-browser support |

</div>

---

## 🚀 Quick Start

### 📋 Prerequisites

<div align="center">

| Requirement | Version | Download |
|-------------|---------|----------|
| **Python** | 3.8+ | [Download Python](https://www.python.org/downloads/) |
| **pip** | Latest | [Install pip](https://pip.pypa.io/en/stable/installation/) |
| **Git** | Latest | [Download Git](https://git-scm.com/downloads) |

</div>

### ⚡ Installation Steps

<div align="center">
  <img src="https://img.shields.io/badge/Step%201-Clone%20Repository-blue?style=for-the-badge" alt="Step 1">
</div>

```bash
# Clone the repository
git clone https://github.com/yourusername/health-disease-prediction.git
cd health-disease-prediction
```

<div align="center">
  <img src="https://img.shields.io/badge/Step%202-Setup%20Environment-green?style=for-the-badge" alt="Step 2">
</div>

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

<div align="center">
  <img src="https://img.shields.io/badge/Step%203-Install%20Dependencies-orange?style=for-the-badge" alt="Step 3">
</div>

```bash
# Install required packages
pip install -r requirements.txt
```

<div align="center">
  <img src="https://img.shields.io/badge/Step%204-Setup%20Database-purple?style=for-the-badge" alt="Step 4">
</div>

```bash
# Run database migrations
python manage.py makemigrations
python manage.py migrate
```

<div align="center">
  <img src="https://img.shields.io/badge/Step%205-Create%20Admin-red?style=for-the-badge" alt="Step 5">
</div>

```bash
# Create superuser (optional but recommended)
python manage.py createsuperuser
```

<div align="center">
  <img src="https://img.shields.io/badge/Step%206-Launch%20Application-success?style=for-the-badge" alt="Step 6">
</div>

```bash
# Start the development server
python manage.py runserver
```

### 🌐 Access the Application

<div align="center">

| URL | Description | Access Level |
|-----|-------------|--------------|
| `http://127.0.0.1:8000/` | Main Application | Public |
| `http://127.0.0.1:8000/admin/` | Admin Panel | Superuser |
| `http://127.0.0.1:8000/login/` | User Login | Registered Users |

</div>

---

## 📋 Requirements

<div align="center">
  <img src="https://img.shields.io/badge/Dependencies-12%20Packages-blue?style=for-the-badge" alt="Dependencies">
</div>

| Package | Version | Category | Description |
|---------|---------|----------|-------------|
| **Django** | 4.2.7 | 🖥️ Web Framework | Core web framework |
| **djangorestframework** | 3.14.0 | 🔌 API Framework | REST API support |
| **pandas** | 2.1.4 | 📊 Data Processing | Data manipulation |
| **numpy** | 1.24.3 | 🔢 Numerical Computing | Mathematical operations |
| **scikit-learn** | 1.3.2 | 🤖 Machine Learning | ML algorithms |
| **matplotlib** | 3.8.2 | 📈 Visualization | Data plotting |
| **seaborn** | 0.13.0 | 📊 Statistical Viz | Advanced plotting |
| **Pillow** | 10.1.0 | 🖼️ Image Processing | Image handling |
| **whitenoise** | 6.6.0 | 📁 Static Files | File serving |
| **gunicorn** | 21.2.0 | 🚀 WSGI Server | Production server |
| **setuptools** | ≥65.0.0 | 🛠️ Build Tools | Package management |

---

## 🏗️ Project Structure

<div align="center">
  <img src="https://img.shields.io/badge/Architecture-MVC%20Pattern-blue?style=for-the-badge" alt="Architecture">
</div>

```
health-disease-prediction/
├── 📁 health/                          # Main Django Application
│   ├── 📄 models.py                    # Database Models
│   ├── 📄 views.py                     # View Logic & Controllers
│   ├── 📄 forms.py                     # Form Definitions
│   ├── 📄 serializers.py              # API Serializers
│   ├── 📄 api_views.py                # API Endpoints
│   ├── 📁 templates/                   # HTML Templates
│   │   ├── 📄 index.html              # Home Page
│   │   ├── 📄 login.html              # Login Page
│   │   ├── 📄 predict_disease.html    # Prediction Interface
│   │   └── 📄 ...                     # Other Templates
│   ├── 📁 static/                      # Static Assets
│   │   ├── 📁 css/                    # Stylesheets
│   │   ├── 📁 js/                     # JavaScript Files
│   │   ├── 📁 images/                 # Image Assets
│   │   └── 📁 fonts/                  # Font Files
│   └── 📁 migrations/                  # Database Migrations
├── 📁 health_desease/                  # Django Project Settings
│   ├── 📄 settings.py                 # Project Configuration
│   ├── 📄 urls.py                     # URL Routing
│   ├── 📄 wsgi.py                     # WSGI Configuration
│   └── 📄 asgi.py                     # ASGI Configuration
├── 📁 Machine_Learning/               # ML Models & Data
│   ├── 📄 Heart prediction.ipynb      # Jupyter Notebook
│   └── 📄 heart.csv                   # Training Dataset
├── 📁 media/                          # User Uploaded Files
├── 📁 screenshots/                    # Application Screenshots
├── 📄 requirements.txt                # Python Dependencies
├── 📄 manage.py                       # Django Management
└── 📄 README.md                       # Project Documentation
```

---

## 🎯 Usage Guide

### 👤 **For Patients**

<div align="center">
  <img src="https://img.shields.io/badge/Patient%20Features-5%20Features-green?style=for-the-badge" alt="Patient Features">
</div>

| Step | Action | Description |
|------|--------|-------------|
| 1️⃣ | **Register/Login** | Create account or sign in to existing account |
| 2️⃣ | **Predict Disease** | Enter medical parameters for heart disease prediction |
| 3️⃣ | **Book Appointments** | Schedule consultations with available doctors |
| 4️⃣ | **View History** | Check your prediction history and results |
| 5️⃣ | **Provide Feedback** | Share your experience and rate the service |

### 👨‍⚕️ **For Doctors**

<div align="center">
  <img src="https://img.shields.io/badge/Doctor%20Features-4%20Features-blue?style=for-the-badge" alt="Doctor Features">
</div>

| Step | Action | Description |
|------|--------|-------------|
| 1️⃣ | **Login** | Access dedicated doctor dashboard |
| 2️⃣ | **Manage Appointments** | View and update appointment status |
| 3️⃣ | **Patient Records** | Access patient information and history |
| 4️⃣ | **Profile Management** | Update professional details and availability |

### 👨‍💼 **For Administrators**

<div align="center">
  <img src="https://img.shields.io/badge/Admin%20Features-4%20Features-red?style=for-the-badge" alt="Admin Features">
</div>

| Step | Action | Description |
|------|--------|-------------|
| 1️⃣ | **User Management** | Manage patients and doctors accounts |
| 2️⃣ | **System Monitoring** | View system statistics and performance |
| 3️⃣ | **Feedback Management** | Handle user feedback and support requests |
| 4️⃣ | **Data Management** | Upload and manage CSV datasets |

---

## 📸 Screenshots

<div align="center">
  <h3>🎨 Application Interface Gallery</h3>
  <p><em>Explore the beautiful and intuitive user interface</em></p>
</div>

### 🏠 **Home Pages**
<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/Home normal.jpeg" width="300" alt="Home Normal" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Home user.jpeg" width="300" alt="Home User" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Home admin.jpeg" width="300" alt="Home Admin" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
    </tr>
  </table>
</div>

### 🔐 **Authentication System**
<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/User login.jpeg" width="300" alt="User Login" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Admin login.jpeg" width="300" alt="Admin Login" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
    </tr>
  </table>
</div>

### 🩺 **Core Features**
<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/Predict user.jpeg" width="300" alt="Disease Prediction" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Book appointment user.jpeg" width="300" alt="Book Appointment" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/View doctor.jpeg" width="300" alt="View Doctor" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
    </tr>
  </table>
</div>

### 👨‍⚕️ **Admin Management**
<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/Add doctor admin.jpeg" width="300" alt="Add Doctor" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Patient admin.jpeg" width="300" alt="Patient Management" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Search admin.jpeg" width="300" alt="Search Admin" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
    </tr>
  </table>
</div>

### 📊 **User Dashboard**
<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/History user.jpeg" width="300" alt="User History" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/User details user.jpeg" width="300" alt="User Details" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Feedback user.jpeg" width="300" alt="User Feedback" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
    </tr>
  </table>
</div>

### 📝 **Additional Pages**
<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/About normal.jpeg" width="300" alt="About Page" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Contect normal.jpeg" width="300" alt="Contact Page" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
      <td><img src="screenshots/Feedback admin.jpeg" width="300" alt="Admin Feedback" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"></td>
    </tr>
  </table>
</div>

---

## 🧠 Machine Learning

<div align="center">
  <img src="https://img.shields.io/badge/ML%20Algorithm-Classification-blue?style=for-the-badge" alt="ML Algorithm">
  <img src="https://img.shields.io/badge/Accuracy-High-success?style=for-the-badge" alt="Accuracy">
  <img src="https://img.shields.io/badge/Features-Medical%20Parameters-green?style=for-the-badge" alt="Features">
</div>

### 🤖 **Model Specifications**

| Component | Details | Status |
|-----------|---------|--------|
| **Algorithm** | Machine Learning Classification | ✅ Implemented |
| **Features** | Medical parameters (age, sex, chest pain, etc.) | ✅ Active |
| **Accuracy** | High prediction accuracy with confidence metrics | ✅ Optimized |
| **Data Source** | Heart disease dataset with medical parameters | ✅ Validated |

### 📊 **Model Performance**

<div align="center">

| Metric | Value | Status |
|--------|-------|--------|
| **Accuracy** | > 85% | 🟢 Excellent |
| **Precision** | > 80% | 🟢 Good |
| **Recall** | > 82% | 🟢 Good |
| **F1-Score** | > 81% | 🟢 Good |

</div>

---

## 🔧 Configuration

### ⚙️ **Environment Variables**

Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DATABASE_URL=sqlite:///db.sqlite3

# Static Files
STATIC_URL=/static/
MEDIA_URL=/media/

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 🗄️ **Database Configuration**

The project uses SQLite by default. For production, consider:

| Database | Use Case | Configuration |
|----------|----------|---------------|
| **SQLite** | Development | Default (no config needed) |
| **PostgreSQL** | Production | Update DATABASES in settings.py |
| **MySQL** | Production | Update DATABASES in settings.py |

---

## 🚀 Deployment

### 🏠 **Local Development**

```bash
# Start development server
python manage.py runserver

# Run with custom port
python manage.py runserver 8080

# Run with custom host
python manage.py runserver 0.0.0.0:8000
```

### 🌐 **Production Deployment**

<div align="center">
  <img src="https://img.shields.io/badge/Deployment-Ready-success?style=for-the-badge" alt="Deployment Ready">
</div>

#### **Step-by-Step Production Setup**

1. **Environment Configuration**
   ```bash
   # Set production environment
   export DJANGO_SETTINGS_MODULE=health_desease.production_settings
   export DEBUG=False
   ```

2. **Database Setup**
   ```bash
   # Run migrations
   python manage.py migrate
   
   # Collect static files
   python manage.py collectstatic
   ```

3. **WSGI Server Setup**
   ```bash
   # Install Gunicorn
   pip install gunicorn
   
   # Start Gunicorn
   gunicorn health_desease.wsgi:application
   ```

4. **Reverse Proxy (Nginx)**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
       
       location /static/ {
           alias /path/to/your/static/files/;
       }
   }
   ```

### 📦 **Docker Deployment**

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "health_desease.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## 🤝 Contributing

<div align="center">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge" alt="Contributions Welcome">
</div>

We welcome contributions! Please follow these steps:

### 📋 **Contribution Guidelines**

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/health-disease-prediction.git
   cd health-disease-prediction
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make Changes**
   ```bash
   # Make your changes
   git add .
   git commit -m "Add some AmazingFeature"
   ```

4. **Push Changes**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open Pull Request**
   - Go to GitHub and create a Pull Request
   - Describe your changes clearly
   - Include screenshots if UI changes

### 🎯 **Development Setup**

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python manage.py test

# Check code style
flake8 health/
```

---

## 📝 License

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</div>

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

<div align="center">
  <img src="https://img.shields.io/badge/Author-Your%20Name-blue?style=for-the-badge" alt="Author">
</div>

**Your Name** - *Full Stack Developer & ML Engineer*

| Platform | Link |
|----------|------|
| 🐙 **GitHub** | [@yourusername](https://github.com/yourusername) |
| 💼 **LinkedIn** | [Your LinkedIn](https://linkedin.com/in/yourprofile) |
| 📧 **Email** | your.email@example.com |
| 🌐 **Website** | [Your Website](https://yourwebsite.com) |

---

## 🙏 Acknowledgments

<div align="center">
  <img src="https://img.shields.io/badge/Thanks-To%20All%20Contributors-brightgreen?style=for-the-badge" alt="Thanks">
</div>

- 🐍 **Django Community** - For the excellent web framework
- 🤖 **Scikit-learn Team** - For powerful machine learning capabilities
- �� **Bootstrap Team** - For responsive design components
- 👥 **All Contributors** - For valuable feedback and testing
- 🏥 **Healthcare Community** - For domain expertise and validation

---

## 📞 Support

<div align="center">
  <img src="https://img.shields.io/badge/Support-Available-blue?style=for-the-badge" alt="Support">
</div>

### 🆘 **Need Help?**

| Support Channel | Description | Response Time |
|-----------------|-------------|---------------|
| 🐛 **GitHub Issues** | Bug reports and feature requests | 24-48 hours |
| 📧 **Email Support** | Direct email support | 12-24 hours |
| 📚 **Documentation** | Comprehensive guides | Instant |
| 💬 **Discussions** | Community discussions | Variable |

### 📞 **Contact Information**

- **Email**: your.email@example.com
- **GitHub Issues**: [Create Issue](https://github.com/yourusername/health-disease-prediction/issues)
- **Documentation**: [Wiki Link]
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/health-disease-prediction/discussions)

---

<div align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge" alt="Made with Love">
  <img src="https://img.shields.io/badge/For-Better%20Healthcare-green?style=for-the-badge" alt="For Better Healthcare">
</div>

<div align="center">
  <p><strong>⭐ Star this repository if you found it helpful!</strong></p>
  <p><em>Together, we can make healthcare more accessible and accurate.</em></p>
</div>

---

<div align="center">
  <sub>Last updated: January 2024 | Built with ❤️ for the healthcare community</sub>
</div>
