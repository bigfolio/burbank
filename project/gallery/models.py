from django.db import models
from django.contrib.auth.models import User
import positions

class Studio(models.Model):
  domain = models.URLField(max_length=200, blank=True)
  joined = models.BooleanField(default=True)
  user = models.ForeignKey(User)
  
  owner_name= models.CharField(max_length=200) 
  business_name = models.CharField(max_length=200) 
  phone = models.CharField(max_length=200) 
  mobile_phone = models.CharField(max_length=200) 
  mobile_domain = models.CharField(max_length=200)
  street_address = models.TextField()
  browser_title = models.TextField()
  site_title = models.CharField(max_length=200)
  email = models.EmailField(max_length=75, blank=True)
  logo_file = models.FileField(upload_to='logos', max_length=100)
  copyright = models.CharField(max_length=200, blank=True)
  meta_description = models.TextField(blank=True)
  meta_keywords = models.TextField(blank=True)
  social_media = models.TextField(blank=True)

  def __unicode__(self):
    return self.business_name

class Gallery(models.Model):
  studio = models.ForeignKey(Studio)
  gallery_name = models.CharField(max_length=200, blank=True)

  #gallery_id = models.IntegerField()
  #category_id = models.IntegerField()
  gallery_name = models.CharField(max_length=200, blank=True)
  gallery_hidden = models.BooleanField(default=False)
  meta_title = models.CharField(max_length=200, blank=True)
  meta_descriptiom = models.TextField(blank=True)
  show_pin_it_button = models.BooleanField(default=True)
  category_name = models.CharField(max_length=100, blank=True)

class Image(models.Model):
  gallery = models.ForeignKey(Gallery)
  image_file = models.CharField(max_length=200, blank=True)
  image_caption = models.CharField(max_length=200, blank=True)
  order_num = positions.PositionField()

