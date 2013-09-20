from pymongo import Connection
import time
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('gallery.html')
db = Connection()
json = db.gallery3.json

allthem = json.find({'domain12' : {'$exists' : True}})
i = 0
l = []
for a in allthem:
  
  try:
    domain = a['domain12']
  except:
    domain = ''
  print domain
  for b in a['galleries']:
    for c in b['images']:
      i += 1
      if i > 100: break
      if domain:
        payload = domain + '/gallery/original/' + c['image_file']
        l.append(payload)
print i,len(l) 
t = template.render(l=l) 
with open('out.html', "wb") as fh:
  fh.write(t.encode('utf8'))


#count = ourmovies.count()

