# go through every mongo studio, create studio, galleries and images
from django.core.management.base import BaseCommand, CommandError
from example.polls.models import Poll
from pymongo import Connection
import time

class Command(BaseCommand):

  def handle(self, *args, **options):
    db = Connection()
    json = db.gallery5.json

    studios = json.find({'domain12' : {'$exists' : True}},limit=10)
    for studio in studios:  
      print 'starting new studio'
      
      new_studio = Studio.objects.create()
      new_studio.domain 
      new_studio.joined
      new_studio.user
      new_studio.owner_name
      new_studio.business_name
      new_studio.phone       
      new_studio.mobile_phone
      new_studio.mobile_domain          
      new_studio.street_address
      new_studio.browser_title
      new_studio.site_title
      new_studio.email
      new_studio.logo_file
      new_studio.copyright
      new_studio.meta_description
      new_studio.meta_keywords
      new_studio.social_media
      new_studio.save()

      for gallery in studio['galleries']:
        
        new_gallery = Gallery.objects.create()
        new_gallery.studio = new_studio
        new_gallery.gallery_name = gallery['gallery_name'] 
        new_gallery.gallery_id = gallery['gallery_id']
        new_gallery.category_id = gallery['category_id'] 
        new_gallery.gallery_name = gallery['category_id'] 
        new_gallery.gallery_hidden = gallery['gallery_name'] 
        new_gallery.meta_title = gallery['meta_title'] 
        new_gallery.meta_descriptiom = gallery['meta_description'] 
        new_gallery.show_pin_it_button = gallery['show_pin_it_button'] 
        new_gallery.category_name = gallery['category_name'] 
        new_gallery.save()

        for image in gallery['images']:
          new_image = Image.objects.create()
          new_image.gallery = image['gallery']
          new_image.image_file = image['image_file']
          new_image.image_caption = image['image_caption']
          new_image.order_num = image['order_num']
          new_image.save()

      self.stdout.write('Successfully closed poll "%s"\n' % poll_id)
