from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
#from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required
from members.models import *
from content.models import *
from django.template import RequestContext
from pymongo import Connection
from bson.objectid import ObjectId

db = Connection()
json = db.gallery.json

def studio(request,_id):
  print _id
  allthem = json.find({'_id':ObjectId(_id)})
  l =[]
  for a in allthem:
    try:
      domain = a['domain12']
    except:
      domain = ''
    for b in a['galleries']:
      for c in b['images']:
        print c['image_file']
        if domain:
          payload = domain + '/gallery/original/' + c['image_file']
          l.append(payload)
  return render_response(request,'studio.html',{'l':l})

def studios(request):
  allthem = json.find()
  l = []
  for x in allthem:
    d = {}
    d['business_name'] = x['business_name']
    d['domain12'] = x['domain12']
    d['meta_description'] = x['meta_description']
    d['id'] = x['_id']
    l.append(d)
  return render_response(request,'studios.html',{'l':l})

#def index(request):
#  return render_response(request,'index.html')
def index(request):
  pages = Page.objects.all()
  
  allthem = json.find({'domain12' : {'$exists' : True}}).skip(10).limit(1)
  i = 0
  l = []
  for a in allthem:
    try:
      domain = a['domain12']
    except:
      domain = ''
    for b in a['galleries']:
      for c in b['images']:
        i += 1
        if i > 10: break
        if domain:
          payload = domain + '/gallery/original/' + c['image_file']
          l.append(payload)

  return render_response(request,'index.html',{'l':l})

def render_response(req, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(req)
  return render_to_response(*args, **kwargs)
