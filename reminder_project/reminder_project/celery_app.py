import os
from celery import Celery
from django.conf import settings

# Встановлюємо модуль Django settings за замовчуванням для програми 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reminder_project.settings')

app = Celery('reminder_project')

# Налаштовуємо конфігурацію додатку з налаштувань Django.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматично знаходимо задачі у всіх зареєстрованих додатках Django.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
