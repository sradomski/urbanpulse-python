"""Main module."""

def get_event_types(credentials):
  from http.client import HTTPSConnection
  from base64 import b64encode
  import json

  c = HTTPSConnection(f"{credentials['host']}")
  headers = { 
    'Authorization' : 'Basic %s' % b64encode(bytes(f"{credentials['username']}:{credentials['password']}", "utf8")).decode("ascii"),
  }
  c.request('GET', '/UrbanPulseManagement/api/eventtypes/', headers=headers)
  data = c.getresponse().read().decode("utf8")
  eventTypes = json.loads(data)
