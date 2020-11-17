from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dsci551(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
