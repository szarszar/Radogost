from django.db import models
from django.conf import settings


class Events(models.Model):

    TYPES = (
        ('Domówka', 'Domówka'),
        ('Na talerzu', 'Na talerzu'),
        ('Na ekranie', 'Na ekranie'),
        ('Na powietrzu', 'Na powietrzu'),
        ('Obalmy rząd', 'Obalmy rząd'),
          )

    name = models.CharField(max_length=64, null=True)
    date = models.DateTimeField(null=True)
    city = models.CharField(max_length=128, null=True)
    street = models.CharField(max_length=64, null=True)
    type = models.CharField(max_length=16, null=True, choices=TYPES)
    description = models.TextField(default='Napisz coś o swoim wydarzeniu')
    coordinates = models.CharField(max_length=128, null=True)
    creatorName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


