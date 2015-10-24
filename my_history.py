import requests
import json
import random

def get_historic_death(month, day):
  response = requests.get('http://history.muffinlabs.com/date/{month}/{day}'.format(month=month,day=day))
  return selected_death(response.text)

def selected_death(response_text):
  deaths = parse_response(response_text)
  seed = random.randrange(1, len(deaths))
  return deaths[seed]

def parse_response(response_text):
  obj = json.loads(response_text)
  deaths = obj['data']['Deaths']
  return deaths
