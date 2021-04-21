from django.db import models
from django.conf import settings


class BirthdayData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
