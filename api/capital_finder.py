from http.server import BaseHTTPRequestHandler
import requests
from urllib import parse

 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)

    if 'country' in my_dict:
      countryName = my_dict.get('country')
      url_cpital = 'https://restcountries.com/v3.1/name/'
      res = requests.get(url_cpital+countryName)
      data = res.json()
      capital = data[0]['capital'][0]
      message = f'The capital of {countryName} is {capital}'

    if 'capital' in my_dict:
      capitalName = my_dict.get('capital')
      url_country = 'https://restcountries.com/v3.1/capital/'
      res = requests.get(url_country+capitalName)
      data = res.json()
      country = data[0]['name']['common']
      message = f'{capitalName} is the capital of {country}'


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(message).encode())
    return