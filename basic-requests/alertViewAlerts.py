import requests
headers = {
  'Accept': 'application/json',
  'X-ZAP-API-Key': 'zap-apikey-1337'
}

r = requests.get('http://localhost:8080/JSON/alert/view/alerts/', params={

}, headers = headers)

print (r.json())