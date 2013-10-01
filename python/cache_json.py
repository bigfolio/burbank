import requests
from pymongo import Connection
import time

def get_domains():
  domains = []
  with open('export.csv') as f:
    for line in f:
      domains.append(line.split('\n')[0])
  return domains

def cache_json(domains):
  db = Connection()
  json = db.gallery5.json
  
  bad_domains = []

  for x in domains:
    try:
      r = requests.get('http://'+str(x)+'/inc/fget_json.php',timeout=3)
      print r.status_code
    except:
      bad_domains.append(x)
      print 'bad',x
      continue

    if r.status_code == 200:
      try:
        payload = r.json()
      except:
        bad_domains.append(x)
        continue
      payload['domain12'] = x
      json.insert(payload, upsert=True)
  return bad_domains

domains = get_domains()
bad = cache_json(domains)

import pickle
outfile = open( "bad_domains", "wb")
pickle.dump(bad, outfile)
