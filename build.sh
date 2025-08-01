#!/usr/bin/env bash
# exit on error
set -o errexit

# Install setuptools first to ensure build dependencies are available
pip install --upgrade pip setuptools wheel

# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
