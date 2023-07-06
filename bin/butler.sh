#!/bin/bash
cd /root/butler
exec /root/butler/env/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
