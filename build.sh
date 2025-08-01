#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Starting build process ==="

# Install setuptools first to ensure build dependencies are available
echo "Installing build dependencies..."
pip install --upgrade pip setuptools wheel

# Install requirements
echo "Installing project dependencies..."
pip install -r requirements.txt

# Run deployment check
echo "Running deployment compatibility check..."
python deploy_check.py

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running database migrations..."
python manage.py migrate

echo "=== Build completed successfully ===" 
