#!/bin/bash
# Startup script for Azure App Service
# Set PYTHONPATH to include the application directory
export PYTHONPATH=/home/site/wwwroot:$PYTHONPATH
# Run gunicorn with the Django application
cd /home/site/wwwroot
exec gunicorn --bind=0.0.0.0 --timeout 600 testing.wsgi:application