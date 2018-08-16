# Преобразование строки времени в формат datetime
# По условию задания нельзя использовать внешние библиотеки
# Лучше конечно было обойтись python-dateutil

import re, datetime

from .regexes import TIME_ISO8601_REGEX

class MyDateTime():
  def __init__(self, date_like_str):
    if not isinstance(date_like_str, str):
      raise TypeError('Is not a string')
    if not self.check_str_for_date(date_like_str):
      raise TypeError('date format is invalid')
    self.str_date = date_like_str
    self.date = self.from_str()

  def check_str_for_date(self, str_obj):
    return re.match(TIME_ISO8601_REGEX, str_obj) is not None

  def from_str(self):
    return datetime.datetime.strptime(self.str_date[:-1].replace('T', ' '), '%Y-%m-%d %H:%M:%S')


# if __name__ == '__main__':
#   time = MyDateTime('2017-12-12T01:02:03Z')
#   print(time.date.isoformat())
#   # MyDateTime('2017-12-01')