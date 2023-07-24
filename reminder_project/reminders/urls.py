from django.urls import path
from reminder_project.reminders.views import create_reminder


app_name = 'reminders'

urlpatterns = [
    path('create-reminder/', create_reminder, name='create-reminder'),  # Шлях для створення нагадування
]

