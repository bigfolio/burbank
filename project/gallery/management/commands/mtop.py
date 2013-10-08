### GALLERY ID NOT BE NULL
# go through every mongo studio, create studio, galleries and images
from django.core.management.base import BaseCommand, CommandError
from gallery.models import *
from django.contrib.auth.models import User
from pymongo import Connection
import time

class Command(BaseCommand):

  def handle(self, *args, **options):
    db = Connection()
    json = db.gallery5.json

    studios = json.find({'domain12' : {'$exists' : True}},limit=10)
    i = 0
    for studio in studios:  
      i += 1
      print 'starting new studio',i
      domain12 = studio.get('domain12','example.com') 
      email = studio.get('email','example@example.com')
      the_user = User.objects.create_user(domain12, email=email)
      new_studio = Studio.objects.create(user_id=the_user.id)
      new_studio.joined = 1
      #new_studio.user = User.objects.get(id=1) 
      new_studio.owner_name = studio.get('owner_name','')
      new_studio.business_name = studio.get('business_name','')
      new_studio.domain = domain12
      new_studio.email = email
      new_studio.phone = studio.get('phone','')     
      new_studio.mobile_phone = studio.get('mobile_phone','')
      new_studio.mobile_domain = studio.get('mobile_domain','')        
      new_studio.street_address = studio.get('street_address','')
      new_studio.browser_title = studio.get('browser_title','')
      new_studio.site_title = studio.get('site_title','')
      new_studio.logo_file = studio.get('logo_file','')
      new_studio.copyright = studio.get('copyright','')
      new_studio.meta_description = studio.get('meta_description','')
      new_studio.meta_keywords = studio.get('meta_keywords','')
      new_studio.social_media = studio.get('social_media','')
      new_studio.save()

      for gallery in studio['galleries']:
        
        new_gallery = Gallery.objects.create(studio=new_studio)
        #new_gallery.studio = new_studio
        new_gallery.gallery_name = gallery['gallery_name'] 
        ######
        #new_gallery.gallery_id = 1
        #new_gallery.category_id = gallery['category_id'] 
        new_gallery.gallery_name = gallery.get('gallery_name','') 
        new_gallery.gallery_hidden = gallery.get('gallery_hidden','') 
        new_gallery.meta_title = gallery.get('meta_title','')
        new_gallery.meta_descriptiom = gallery.get('meta_description','')
        new_gallery.show_pin_it_button = gallery.get('show_pin_it_button',0)
        new_gallery.category_name = gallery.get('category_name','') 
        new_gallery.save()

        for image in gallery['images']:
         
          new_image = Image.objects.create(gallery=new_gallery)
          #new_image.gallery = image['gallery']
          new_image.image_file = image.get('image_file','')
          new_image.image_caption = image.get('image_caption','')
          new_image.order_num = image.get('order_num','')
          new_image.save()

      self.stdout.write('Successfully closed poll')
