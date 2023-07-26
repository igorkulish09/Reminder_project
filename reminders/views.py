from django.shortcuts import render, redirect
from django.core.mail import send_mail
from celery import shared_task
from django.contrib import messages
from .models import Reminder
from .models import Author
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.db.models import Count


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


@cache_page(60 * 15)
def author_list(request):

    authors = Author.objects.all()

    authors_with_books_count = authors.annotate(num_books=Count('book'))

    authors_with_books = authors_with_books_count.filter(num_books__gt=0)

    paginator = Paginator(authors_with_books, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'author_list.html', {'page_obj': page_obj})
