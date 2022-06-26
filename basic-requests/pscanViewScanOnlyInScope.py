#!/usr/bin/env python
import requests
headers = {
  'Accept': 'application/json',
  'X-ZAP-API-Key': 'zap-api-1337'
}

r = requests.get('http://localhost:8080/JSON/pscan/view/scanOnlyInScope/', params={

}, headers = headers)

print (r.json())