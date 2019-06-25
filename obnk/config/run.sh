#!/bin/bash

# Wait for postgresql container
/wait-for.sh postgres 5432

# Migrate database and collectstatic
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
echo "from obnk_apps.users.models import User; User.objects.filter(email='admin@obnk.com').delete(); User.objects.create_superuser('admin@obnk.com', 'obnk2019')" | python manage.py shell
# Run gunicorn for django server
gunicorn obnk.wsgi -b 0.0.0.0:8001 --reload