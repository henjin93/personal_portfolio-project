from pyexpat import model
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    article = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    date = models.DateField()
