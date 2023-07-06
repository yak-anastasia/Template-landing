#Create file config.py with this setting or rename this file to config.py

#BASE
DEBUG=True
SECRET_KEY='secret-key(absolutely any character)'
ALLOWED_HOSTS = ['127.0.0.1']
CSRF_TRUSTED_ORIGINS = []

#DATABSE
DB_NAME=None
DB_USER=None
DB_PASSWORD=None
DB_HOST=None

#GUNICORN
BIND = "127.0.0.1:8000"
WORKERS = 1
THREADS = 2

#EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.sharix-app.org'
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'example@sharix-app.org'
EMAIL_HOST_PASSWORD = '**************'
EMAIL_TO = 'example@sharix-app.org'

#STATIC
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "butler/static/"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"