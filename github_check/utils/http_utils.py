# Обертка для запроса и ответа от api github
# Пошел прортив правил, использую внешнюю requests.
# пробовал httplib, но не разобрался как отправлять https request
# почитал литературу - написано, что python должен быть скомпилирован с поддержкой ssl

import requests, json, re

from github_check.utils.regexes import URL_REGEX, REL_REGEX

class GResponse():
  def __init__(self, response):
    self.status = response.status_code
    self.parse_links(response.headers)
    self.content = response.json()
    self.count_items_per_page = len(self.content)

  def parse_links(self, header):
    self.links = dict()
    h_links = header.get('Link')
    if h_links is not None:
      rel = re.findall(REL_REGEX, h_links)
      url = re.findall(URL_REGEX, h_links)
      self.links.update(zip(rel, url))

  def __repr__(self):
    return "status: {status}\ncontent length: {count_of_items}\nlinks:\n{links}".format(**{
      'status':self.status,
      'count_of_items': self.count_items_per_page,
      'links': json.dumps(self.links, indent=4),
    })


class GRequest():

  def __init__(self, url: str, payload = None):
    r = requests.get(url, params = payload)
    self.response = GResponse(r) if r.status_code == requests.codes.ok else None


if __name__ == '__main__':
  response = GRequest('https://api.github.com/repos/lexapin/employees').response
  print(response)
  # print(json.dumps(response.content, indent=4))
  new_response = GRequest(response.content['contributors_url']).response
  print(new_response)
  print(json.dumps(new_response.content, indent=4))