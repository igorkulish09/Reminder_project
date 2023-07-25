from django import forms
from .models import Reminder


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['email', 'text', 'reminder_time']


