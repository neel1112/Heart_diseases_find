# 🏥 Heart Disease Prediction System

[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive **Heart Disease Prediction System** built with Django and Machine Learning that helps users predict heart disease risk based on medical parameters. The system includes user management, doctor appointments, and an intelligent prediction model.

## 🌟 Features

### 🔬 **Core Functionality**
- **Heart Disease Prediction**: ML-powered risk assessment using medical parameters
- **User Management**: Separate interfaces for patients, doctors, and administrators
- **Appointment System**: Book and manage doctor appointments
- **Search & History**: Track prediction history and search functionality
- **Feedback System**: User feedback and rating system

### 👥 **User Roles**
- **Patients**: Register, predict disease risk, book appointments
- **Doctors**: Manage appointments, view patient records
- **Administrators**: Manage users, doctors, and system data

### 🎯 **Key Features**
- Real-time disease prediction with accuracy metrics
- Responsive web interface
- Secure authentication system
- File upload and management
- Comprehensive admin dashboard
- Mobile-friendly design

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd health-disease-prediction
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📋 Requirements

| Package | Version | Description |
|---------|---------|-------------|
| Django | 4.2.7 | Web framework |
| djangorestframework | 3.14.0 | REST API framework |
| pandas | 2.1.4 | Data manipulation |
| numpy | 1.24.3 | Numerical computing |
| scikit-learn | 1.3.2 | Machine learning |
| matplotlib | 3.8.2 | Data visualization |
| seaborn | 0.13.0 | Statistical visualization |
| Pillow | 10.1.0 | Image processing |
| whitenoise | 6.6.0 | Static file serving |
| gunicorn | 21.2.0 | WSGI server |

## 🏗️ Project Structure

```
health-disease-prediction/
├── health/                    # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── forms.py              # Form definitions
│   ├── templates/            # HTML templates
│   ├── static/               # CSS, JS, images
│   └── migrations/           # Database migrations
├── health_desease/           # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── Machine_Learning/         # ML models and data
│   ├── Heart prediction.ipynb
│   └── heart.csv
├── media/                    # User uploaded files
├── screenshots/              # Application screenshots
└── requirements.txt          # Python dependencies
```

## 🎯 Usage Guide

### For Patients
1. **Register/Login**: Create an account or sign in
2. **Predict Disease**: Enter medical parameters for heart disease prediction
3. **Book Appointments**: Schedule consultations with doctors
4. **View History**: Check your prediction history
5. **Provide Feedback**: Share your experience

### For Doctors
1. **Login**: Access doctor dashboard
2. **Manage Appointments**: View and update appointment status
3. **Patient Records**: Access patient information
4. **Profile Management**: Update professional details

### For Administrators
1. **User Management**: Manage patients and doctors
2. **System Monitoring**: View system statistics
3. **Feedback Management**: Handle user feedback
4. **Data Management**: Upload and manage CSV files

## 📸 Application Screenshots

### 🏠 Home Pages
<div align="center">
  <img src="screenshots/Home normal.jpeg" width="300" alt="Home Normal">
  <img src="screenshots/Home user.jpeg" width="300" alt="Home User">
  <img src="screenshots/Home admin.jpeg" width="300" alt="Home Admin">
</div>

### 🔐 Authentication
<div align="center">
  <img src="screenshots/User login.jpeg" width="300" alt="User Login">
  <img src="screenshots/Admin login.jpeg" width="300" alt="Admin Login">
</div>

### 🩺 Core Features
<div align="center">
  <img src="screenshots/Predict user.jpeg" width="300" alt="Disease Prediction">
  <img src="screenshots/Book appointment user.jpeg" width="300" alt="Book Appointment">
  <img src="screenshots/View doctor.jpeg" width="300" alt="View Doctor">
</div>

### 👨‍⚕️ Admin Features
<div align="center">
  <img src="screenshots/Add doctor admin.jpeg" width="300" alt="Add Doctor">
  <img src="screenshots/Patient admin.jpeg" width="300" alt="Patient Management">
  <img src="screenshots/Search admin.jpeg" width="300" alt="Search Admin">
</div>

### 📊 User Features
<div align="center">
  <img src="screenshots/History user.jpeg" width="300" alt="User History">
  <img src="screenshots/User details user.jpeg" width="300" alt="User Details">
  <img src="screenshots/Feedback user.jpeg" width="300" alt="User Feedback">
</div>

### 📝 Additional Pages
<div align="center">
  <img src="screenshots/About normal.jpeg" width="300" alt="About Page">
  <img src="screenshots/Contect normal.jpeg" width="300" alt="Contact Page">
  <img src="screenshots/Feedback admin.jpeg" width="300" alt="Admin Feedback">
</div>

## 🧠 Machine Learning Model

The heart disease prediction model uses:
- **Algorithm**: Machine Learning classification
- **Features**: Medical parameters (age, sex, chest pain, etc.)
- **Accuracy**: High prediction accuracy with confidence metrics
- **Data Source**: Heart disease dataset with medical parameters

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration
The project uses SQLite by default. For production, consider PostgreSQL or MySQL.

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. Set `DEBUG = False` in settings
2. Configure production database
3. Set up static file serving
4. Use Gunicorn as WSGI server
5. Configure reverse proxy (Nginx)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Scikit-learn for machine learning capabilities
- Bootstrap for responsive design components
- All contributors and testers

## 📞 Support

If you have any questions or need support:
- Create an issue in the repository
- Contact: your.email@example.com
- Documentation: [Wiki Link]

---

<div align="center">
  <p>Made with ❤️ for better healthcare</p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>
