python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate && gunicorn -b 0.0.0.0:8000 -w 2 config.wsgi --access-logfile $G_ACCESS_LOGS --error-logfile $G_ERROR_LOGS --reload