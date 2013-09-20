from django.db import models

class Content(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  chapter = models.IntegerField()
  front_page = models.BooleanField()

class Page(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  order = models.IntegerField()
