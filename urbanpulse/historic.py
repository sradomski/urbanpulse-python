"""Main module."""

def fetch_csv(credentials, sid, start_date, end_date):
  import datetime
  import pytz
  from http.client import HTTPSConnection
  from base64 import b64encode

  start_date = pytz.UTC.localize(start_date)
  end_date = pytz.UTC.localize(end_date) 

  c = HTTPSConnection(f"{credentials['host']}:42000")
  headers = { 
    'Authorization' : 'Basic %s' % b64encode(bytes(f"{credentials['username']}:{credentials['password']}", "utf8")).decode("ascii"),
    'Accept' : 'text/csv'
  }
  historicBase = "/UrbanPulseData/historic/sensordata?"

  url = historicBase + "since={}Z&until={}Z&sid={}".format(
    start_date.isoformat()[:-9],
    end_date.isoformat()[:-9], 
    sid)
  print(url)
  c.request('GET', url, headers=headers)
  data = c.getresponse().read().decode("utf8")
  return data