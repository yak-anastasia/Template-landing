# Template landing

## How install?

1. Download or clone repository
```bash
git https://github.com/yak-anastasia/Template-landing.git
git checkout unstable
```
2. Set up a configuration file
```python
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

#STATIC
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "SharixAdmin/static/", BASE_DIR / "tickets/static/"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
3. Run a **install_unix.sh** if you have Linux or if you have Windows run a **install_win.sh**
4. The system will prompt you to create a superuser
```
#Example
7987654321
admin
pa$$w0rd
pa$$w0rd
```
5. Start test the server:
```
python manage.py runserver 8000
```
6. Set up the **bin/butler.sh** file with valid paths

```bash
#!/bin/bash
cd /path/to/project
exec /path/to/project/env/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
```
7. It remains to configure Nginx conf and start the daemon

