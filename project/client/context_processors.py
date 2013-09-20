from content.models import *

def seo(request):
  try:
    pages = Page.objects.all()
  except:
    pages = {}
  return {'pages': pages}
