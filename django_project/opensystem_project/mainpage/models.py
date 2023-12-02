from django.db import models
class Request(models.Model):
    query = models.CharField(max_length=255)
# Create your models here.
