from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()  # Поле для тексту відгуку
    created_at = models.DateTimeField(default=timezone.now)  # Час створення відгуку

    def __str__(self):
        return self.text[:50]  # Виводимо початковий текст відгуку для зручності
