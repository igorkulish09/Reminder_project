from django.db import models


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField()
    reminder_time = models.DateTimeField()


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Book(models.Model):
     tittle = models.CharField(max_length=200)
     author = models.ForeignKey(Author, on_delete=models.CASCADE)
