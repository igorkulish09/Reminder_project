from celery import Celery

# Create the Celery app object
celery = Celery('reminders')

# Load the default configuration from Django settings
celery.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in all registered Django app configs
celery.autodiscover_tasks()

# You can add any additional Celery configurations here if needed

# This ensures that the app is loaded when Django starts
__all__ = ('celery',)
