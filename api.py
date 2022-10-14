from requests import Request, Session
import os
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://api.coingecko.com/api/v3/coins/dogecoin?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false'
# parameters = {
#   'start':'150',
#   'limit':'160',
#   'convert':'USD',
#   'cryptocurrency_type':'coins',
#   'sort':'symbol'
# }
headers = {
  'Accepts': 'application/json',
  #'X-CMC_PRO_API_KEY': os.getenv('TOKEN'),
}

session = Session()
session.headers.update(headers)

def update():
  try:
    response = session.get(url)
    data = json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as exception:
    print(exception)
  return data['market_data']['current_price']['usd']
