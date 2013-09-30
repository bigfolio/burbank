import requests
import sys
import time

def get_domains():
  domains = []
  with open('export.csv') as f:
    for line in f:
      domains.append(line.split('\n')[0])

  return domains

def cache_json(domains):
  bad_domains = []
  for x in domains:
    try:
      r = requests.get('http://'+str(x)+'/inc/fget_json.php',timeout=3)
    except KeyboardInterrupt:
      raise
    except:
      print "Unexpected error:", sys.exc_info()[0],x
      bad_domains.append(x)
      continue

    if r.status_code == 200:
      try:
        payload = r.json()
      except:
        bad_domains.append(x)
        continue
    else: print r.status_code,x

  return bad_domains

domains = get_domains()
bad = cache_json(domains)

import pickle
outfile = open( "bad_domainswrong", "wb")
pickle.dump(bad, outfile)
