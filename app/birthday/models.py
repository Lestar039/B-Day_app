from django.db import models
from django.conf import settings
from django.urls import reverse


class BirthdayData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_url', kwargs={'pk': self.pk})
