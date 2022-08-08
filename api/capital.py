from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    

    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    query_dict = dict(query_string_list)

    if "capital" in query_dict:
      url = "https://restcountries.com/v3.1/capital/"
      response = requests.get(url + query_dict["capital"])
      data = response.json()
      country_names = []
      capital_name = []
      for country_data in data:
        capital = country_data["capital"][0]
        capital_name.append(capital)
        name = country_data["name"]["official"]
        country_names.append(name)
      message = f"{str(capital_name[0])} is the capitol of the {str(country_names[0])}"
    else:
      message = "Give me a word"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()


    self.wfile.write(message.encode())
    return