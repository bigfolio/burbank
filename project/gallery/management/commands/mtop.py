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
    for studio in studios:  
      print 'starting new studio'
      new_studio = Studio.objects.create(user_id=1)
      new_studio.domain = studio['domain12'] 
      new_studio.joined = 1
      new_studio.user = User.objects.get(id=1) 
      new_studio.owner_name = studio['owner_name']
      new_studio.business_name = studio['business_name']
      new_studio.phone = studio['phone']     
      new_studio.mobile_phone = studio['mobile_phone']
      new_studio.mobile_domain = studio['mobile_domain']        
      new_studio.street_address = studio['street_address']
      new_studio.browser_title = studio['browser_title']
      new_studio.site_title = studio['site_title']
      new_studio.email = studio['email']
      new_studio.logo_file = studio['logo_file']
      new_studio.copyright = studio['copyright']
      new_studio.meta_description = studio['meta_description']
      new_studio.meta_keywords = studio['meta_keywords']
      new_studio.social_media = studio['social_media']
      new_studio.save()

      for gallery in studio['galleries']:
        
        new_gallery = Gallery.objects.create(studio=new_studio)
        #new_gallery.studio = new_studio
        new_gallery.gallery_name = gallery['gallery_name'] 
        ######
        new_gallery.gallery_id = 1
        new_gallery.category_id = gallery['category_id'] 
        new_gallery.gallery_name = gallery['category_id'] 
        new_gallery.gallery_hidden = gallery['gallery_name'] 
        new_gallery.meta_title = gallery['meta_title'] 
        new_gallery.meta_descriptiom = gallery['meta_description'] 
        new_gallery.show_pin_it_button = gallery['show_pin_it_button'] 
        new_gallery.category_name = gallery['category_name'] 
        new_gallery.save()

        for image in gallery['images']:
         
          new_image = Image.objects.create(gallery=new_gallery)
          #new_image.gallery = image['gallery']
          new_image.image_file = image['image_file']
          new_image.image_caption = image['image_caption']
          new_image.order_num = image['order_num']
          new_image.save()

      self.stdout.write('Successfully closed poll "%s"\n' % poll_id)
