# Heart Disease Prediction System

A Django-based web application for predicting heart diseases using machine learning algorithms.

## Features

- User authentication and authorization
- Doctor and patient management
- Heart disease prediction using ML models
- Appointment scheduling system
- Feedback system
- Admin dashboard

## Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite3
- **ML Libraries**: scikit-learn, pandas, numpy
- **Frontend**: HTML, CSS, Bootstrap
- **Deployment**: Render.com

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/neel1112/Heart_diseases_find.git
cd Heart_diseases_find
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Open http://localhost:8000 in your browser

## Deployment

### Render.com Deployment

1. Connect your GitHub repository to Render
2. Set the following environment variables:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False for production
3. Set build command: `./build.sh`
4. Set start command: `gunicorn health_desease.wsgi:application`

### Environment Variables

- `SECRET_KEY`: Django secret key for production
- `DEBUG`: Set to 'False' for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Project Structure

```
├── health/                 # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── templates/         # HTML templates
│   └── static/           # Static files (CSS, JS, images)
├── health_desease/        # Django project settings
│   ├── settings.py       # Development settings
│   ├── production_settings.py  # Production settings
│   └── urls.py           # URL configuration
├── Machine_Learning/      # ML models and data
├── requirements.txt       # Python dependencies
├── build.sh              # Build script for deployment
└── runtime.txt           # Python version specification
```

## Recent Updates

### Version 4.2.7 Compatibility

- Updated Django from 3.1.6 to 4.2.7
- Updated all dependencies to compatible versions
- Removed deprecated `USE_L10N` setting
- Added `DEFAULT_AUTO_FIELD` setting
- Fixed model compatibility issues
- Enhanced build script with better error handling

## Troubleshooting

### Common Issues

1. **Build fails with setuptools error**: Ensure you're using Python 3.11+ and the updated requirements.txt
2. **Database migration errors**: Run `python manage.py makemigrations` followed by `python manage.py migrate`
3. **Static files not loading**: Run `python manage.py collectstatic`

### Deployment Issues

- Check the build logs in Render dashboard
- Ensure all environment variables are set correctly
- Verify the Python version in runtime.txt matches your deployment platform

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

