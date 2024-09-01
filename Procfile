
web: gunicorn verceldeploy.wsgi --log-file - 

web: python manage.py migrate && gunicorn verceldeploy.wsgi