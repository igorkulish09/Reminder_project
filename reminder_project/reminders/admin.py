from django.contrib import admin
from .models import Author, Quote
from .tasks import add_new_quotes
from django_celery_beat.models import PeriodicTask


class PeriodicTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'task', 'enabled', 'interval', 'next_run_at']
    list_editable = ['enabled', 'interval', 'next_run_at']


admin.site.register(Author)
admin.site.register(Quote)
