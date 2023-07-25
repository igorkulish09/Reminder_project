from django.shortcuts import render, redirect
from django.core.mail import send_mail
from celery import shared_task
from django.contrib import messages
from .models import Reminder


@shared_task
def send_reminder_email(email, text):
    send_mail('Нагадування', text, 'your_email@example.com', [email])


def create_reminder(request):
    if request.method == 'POST':
        email = request.POST['email']
        reminder_text = request.POST['reminder_text']
        reminder_datetime = request.POST['reminder_datetime']

        send_reminder_email.apply_async(args=[email, reminder_text], eta=reminder_datetime)

        messages.success(request, 'Нагадування було успішно створено!')

        return redirect('reminders:create-reminder')

    return render(request, "reminders/reminder_form.html")


def reminders_detail(request, pk):
    reminder = Reminder.objects.get(pk=pk)
    context = {
        'reminder': reminder,
    }

    return render(request, "reminders/reminders_created.html", context)


