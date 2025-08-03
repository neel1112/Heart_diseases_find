# 🏥 Heart Disease Prediction System

A comprehensive healthcare platform that uses Machine Learning to predict heart disease risk based on medical parameters. Built with Django and Python, this system provides separate interfaces for patients, doctors, and administrators.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Machine Learning Model](#machine-learning-model)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Support](#support)

## Overview

This Heart Disease Prediction System is designed to help users assess their risk of heart disease using machine learning algorithms. The platform includes:

- **Patient Portal**: Register, predict disease risk, book appointments
- **Doctor Portal**: Manage appointments and patient records
- **Admin Portal**: System management and user administration
- **ML Prediction Engine**: Real-time heart disease risk assessment

### Key Technologies

- **Backend**: Django 4.2.7 (Python web framework)
- **Machine Learning**: Scikit-learn, NumPy, Pandas
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Deployment**: Gunicorn, Nginx

## Features

### Core Functionality

1. **Heart Disease Prediction**
   - Input medical parameters (age, sex, chest pain, blood pressure, etc.)
   - Real-time ML-powered risk assessment
   - Accuracy metrics and confidence scores
   - Historical prediction tracking

2. **User Management System**
   - Patient registration and profile management
   - Doctor account creation and verification
   - Admin user management and system monitoring
   - Role-based access control

3. **Appointment System**
   - Book appointments with available doctors
   - Appointment status tracking (pending, confirmed, cancelled, completed)
   - Doctor availability management
   - Appointment history and notifications

4. **Search and History**
   - Search for doctors by specialty
   - View prediction history with detailed results
   - Track medical parameters over time
   - Export prediction reports

5. **Feedback System**
   - User feedback collection
   - Rating system for doctors and services
   - Admin feedback management
   - Quality improvement tracking

### User Roles

#### Patients
- Register and manage personal accounts
- Enter medical parameters for heart disease prediction
- Book appointments with available doctors
- View prediction history and detailed results
- Provide feedback and ratings
- Update personal information and medical details
- Access educational resources about heart health

#### Doctors
- Access dedicated doctor dashboard
- Manage patient appointments and schedules
- View patient records and medical history
- Update appointment status and add notes
- Manage professional profile and availability
- Access patient prediction results
- Communicate with patients through the platform

#### Administrators
- Complete system management and monitoring
- Manage users, doctors, and patient accounts
- Upload and manage medical datasets
- Monitor system performance and analytics
- Handle user feedback and support requests
- Configure system settings and parameters
- Generate system reports and statistics

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/health-disease-prediction.git
   cd health-disease-prediction
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   # Create database migrations
   python manage.py makemigrations
   
   # Apply migrations
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Application**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 4.2.7 | Web framework |
| djangorestframework | 3.14.0 | REST API support |
| pandas | 2.1.4 | Data manipulation |
| numpy | 1.24.3 | Numerical computing |
| scikit-learn | 1.3.2 | Machine learning |
| matplotlib | 3.8.2 | Data visualization |
| seaborn | 0.13.0 | Statistical visualization |
| Pillow | 10.1.0 | Image processing |
| whitenoise | 6.6.0 | Static file serving |
| gunicorn | 21.2.0 | Production server |

## Usage

### For Patients

1. **Registration/Login**
   - Visit the main application
   - Click "Register" to create a new account
   - Fill in personal information and medical details
   - Verify email (if configured)

2. **Disease Prediction**
   - Navigate to "Predict Disease" section
   - Enter required medical parameters:
     - Age, Sex, Chest Pain Type
     - Blood Pressure, Cholesterol
     - Fasting Blood Sugar
     - ECG Results, Heart Rate
     - Exercise Angina, ST Depression
   - Submit for ML analysis
   - View prediction results with confidence score

3. **Booking Appointments**
   - Browse available doctors
   - Select preferred doctor and time slot
   - Provide symptoms and reason for visit
   - Confirm appointment booking
   - Receive confirmation notification

4. **Viewing History**
   - Access "My History" section
   - View all previous predictions
   - Track parameter changes over time
   - Download prediction reports

### For Doctors

1. **Login and Dashboard**
   - Access doctor portal with credentials
   - View upcoming appointments
   - Check patient messages and requests

2. **Appointment Management**
   - View all scheduled appointments
   - Update appointment status
   - Add notes and recommendations
   - Manage availability calendar

3. **Patient Records**
   - Access patient medical history
   - View prediction results and trends
   - Add medical notes and observations
   - Track patient progress

### For Administrators

1. **User Management**
   - Add/remove doctors and patients
   - Verify doctor credentials
   - Manage user permissions
   - Monitor user activity

2. **System Monitoring**
   - View system statistics
   - Monitor prediction accuracy
   - Track user engagement
   - Generate performance reports

3. **Data Management**
   - Upload new training datasets
   - Update ML model parameters
   - Backup and restore data
   - Manage system configurations

## Screenshots

### Home Pages
- **Public Home**: Landing page with system overview
- **Patient Home**: Personalized dashboard for patients
- **Admin Home**: System management interface

### Authentication
- **User Login**: Patient and doctor login interface
- **Admin Login**: Administrator access portal

### Core Features
- **Disease Prediction**: ML prediction interface
- **Appointment Booking**: Doctor appointment system
- **Doctor Directory**: Available doctors listing

### Admin Management
- **Add Doctor**: Doctor registration interface
- **Patient Management**: Patient account administration
- **Search Admin**: Advanced search functionality

### User Features
- **History View**: Prediction history tracking
- **User Details**: Profile management
- **Feedback System**: User feedback collection

## Machine Learning Model

### Model Specifications

- **Algorithm**: Machine Learning Classification
- **Training Data**: Heart disease dataset with medical parameters
- **Features**: 13 medical parameters including age, sex, chest pain type, blood pressure, cholesterol, etc.
- **Output**: Binary classification (heart disease risk: yes/no) with confidence score

### Model Performance

| Metric | Value | Status |
|--------|-------|--------|
| Accuracy | > 85% | Excellent |
| Precision | > 80% | Good |
| Recall | > 82% | Good |
| F1-Score | > 81% | Good |

### Medical Parameters Used

1. **Age**: Patient age in years
2. **Sex**: Gender (male/female)
3. **Chest Pain Type**: Type of chest pain experienced
4. **Resting Blood Pressure**: Blood pressure at rest
5. **Serum Cholesterol**: Cholesterol level in mg/dl
6. **Fasting Blood Sugar**: Blood sugar level
7. **ECG Results**: Electrocardiogram results
8. **Max Heart Rate**: Maximum heart rate achieved
9. **Exercise Angina**: Exercise-induced angina
10. **ST Depression**: ST depression induced by exercise
11. **Slope**: Slope of peak exercise ST segment
12. **Number of Vessels**: Number of major vessels colored
13. **Thalassemia**: Thalassemia type

## Configuration

### Environment Variables

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

### Database Configuration

The project uses SQLite by default. For production deployment:

**PostgreSQL Configuration:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**MySQL Configuration:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Deployment

### Local Development

```bash
# Start development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### Production Deployment

1. **Environment Setup**
   ```bash
   # Set production environment
   export DJANGO_SETTINGS_MODULE=health_desease.production_settings
   export DEBUG=False
   ```

2. **Database Migration**
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
   gunicorn health_desease.wsgi:application --bind 0.0.0.0:8000
   ```

4. **Nginx Configuration**
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
       
       location /media/ {
           alias /path/to/your/media/files/;
       }
   }
   ```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start application
CMD ["gunicorn", "health_desease.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=health_db
      - POSTGRES_USER=health_user
      - POSTGRES_PASSWORD=health_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

## Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/health-disease-prediction.git
   cd health-disease-prediction
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   ```bash
   # Make your changes
   git add .
   git commit -m "Add your feature description"
   ```

4. **Push Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Go to GitHub and create a Pull Request
   - Describe your changes clearly
   - Include screenshots if UI changes

### Development Guidelines

- Follow PEP 8 Python style guidelines
- Write clear commit messages
- Add tests for new features
- Update documentation as needed
- Test thoroughly before submitting

## Support

### Getting Help

- **GitHub Issues**: Report bugs and request features
- **Email Support**: Direct support via email
- **Documentation**: Comprehensive guides and tutorials
- **Community**: Join discussions and ask questions

### Contact Information

- **Email**: your.email@example.com
- **GitHub Issues**: [Create Issue](https://github.com/yourusername/health-disease-prediction/issues)
- **Documentation**: [Wiki Link]
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/health-disease-prediction/discussions)

### Common Issues and Solutions

1. **Database Migration Errors**
   ```bash
   python manage.py makemigrations --merge
   python manage.py migrate
   ```

2. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic
   ```

3. **Import Errors**
   ```bash
   pip install -r requirements.txt
   ```

4. **Port Already in Use**
   ```bash
   python manage.py runserver 8080
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Your Name** - Full Stack Developer & ML Engineer

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- **Email**: your.email@example.com
- **Website**: [Your Website](https://yourwebsite.com)

## Acknowledgments

- Django community for the excellent web framework
- Scikit-learn team for powerful machine learning capabilities
- Bootstrap team for responsive design components
- All contributors and testers for valuable feedback
- Healthcare community for domain expertise and validation

---

**Made with ❤️ for better healthcare**

*Star this repository if you found it helpful!*
