from celery import shared_task
from .models import Author, Quote
from articles.utils import get_new_quotes


@shared_task
def add_new_quotes():
    new_quotes = get_new_quotes()
    for quote_data in new_quotes:
        author, _ = Author.objects.get_or_create(name=quote_data["author"], bio=quote_data["bio"])
        Quote.objects.create(text=quote_data["text"], author=author)
