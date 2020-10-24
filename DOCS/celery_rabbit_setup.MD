<!-- $ sudo rabbitmq-server -detached -->
# 1) Install RabbitMQ
### For Ubuntu
❯ apt-get install -y erlang
❯ apt-get install rabbitmq-server

### To start/stop the RabbitMQ service:
❯ systemctl enable rabbitmq-server
❯ systemctl start rabbitmq-server
❯ systemctl status rabbitmq-server​
❯ systemctl stop rabbitmq-server

### Add user settings 
❯ sudo rabbitmqctl add_user celeryuser celerypassword
❯ sudo rabbitmqctl add_vhost celeryhost
❯ sudo rabbitmqctl set_permissions -p celeryhost celeryuser ".*" ".*" ".*"

# 2) Setup the Virtual Environment and install requirements. 
❯ sudo apt install virtualenv
❯ virtualenv venv -p python3
❯ source venv/bin/activate
❯ pip install -r requirements.txt

# 3) Start a Django application 
❯ django-admin startproject myproject
❯ cd myproject
❯ python manage.py startapp myapp
❯ create superuser: python manage.py createsuperuser

# 4) Add installed apps and run migrations 
❯ add "myapp" and "django_celery_beat" to myproject/settings.py INSTALLED_APPS


# Create a Celery instance file called celery.py . Create this file at the same level of settings.py file and add the following:

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()



