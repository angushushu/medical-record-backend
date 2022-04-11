from django.db import models

# Create your models here.
class Specialty1(models.Model):
    value = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=32, default='', blank=True)
    description = models.TextField(max_length=256, default='', blank=True)

    class Meta:
        ordering = ('value',)
    def __str__(self):
        return self.org_name
class Specialty2(models.Model):


class Specialty3(models.Model):