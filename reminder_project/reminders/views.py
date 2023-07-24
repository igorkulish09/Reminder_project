from django.shortcuts import render
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_reminder_email(email, text):
    send_mail('Нагадування', text, 'your_email@example.com', [email])


def create_reminder(request):
    if request.method == 'POST':
        email = request.POST['email']
        reminder_text = request.POST['reminder_text']
        reminder_datetime = request.POST['reminder_datetime']

        send_reminder_email.apply_async(args=[email, reminder_text], eta=reminder_datetime)

        return render(request, 'magazine/reminder_form.html')

    return render(request, 'magazine/reminder_form.html')

