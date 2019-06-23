from django.db import models
from django.utils import timezone


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    postalCode = models.CharField(max_length=10)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    websiteUrl = models.CharField(max_length=200)
    facebookUrl = models.CharField(max_length=200)
    cityName = models.CharField(max_length=200)

    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
