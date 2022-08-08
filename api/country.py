from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    

    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    query_dict = dict(query_string_list)

    if "name" in query_dict:
      url = "https://restcountries.com/v3.1/name/"
      response = requests.get(url + query_dict["name"])
      data = response.json()
      capital_names = []
      country_name = []
      for country_data in data:
        capital = country_data["capital"][0]
        capital_names.append(capital)
        name = country_data["name"]["official"]
        country_name.append(name)
      message = f"The capitol of {str(country_name[0])} is {str(capital_names[0])}"
    else:
      message = "Give me a word"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()


    self.wfile.write(message.encode())
    return