# Обертка для запроса и ответа от api github
# Пошел прортив правил, использую внешнюю requests

import requests, json, re

regex_url = re.compile(r'(?<=<).*?(?=>)', re.IGNORECASE)
regex_rel = re.compile(r'(?<=rel=").*?(?=")', re.IGNORECASE)

class GResponse():
  def __init__(self, response):
    self.parse_links(response.headers)
    self.count_items_per_page = len(json.loads(response.content))

  def parse_links(self, header):
    self.links = dict()
    h_links = header.get('Link')
    if h_links is not None:
      rel = re.findall(regex_rel, h_links)
      url = re.findall(regex_url, h_links)
      print(rel)
      print(url)


class GRequest():

  def __init__(self, url=None):
    self.response = GResponse(requests.get('https://api.github.com/repos/lexapin/employees/commits'))


if __name__ == '__main__':
  GRequest()