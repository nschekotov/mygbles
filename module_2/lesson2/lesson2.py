'''1. Получить количество учеников с сайта geekbrains.ru:
a) при помощи регулярных выражений,
b) при помощи библиотеки BeautifulSoup.'''

import requests
import re
from bs4 import BeautifulSoup

url = 'https://geekbrains.ru/'
resp = requests.get(url)
first_text = resp.text


studentsre = re.findall('<span class="total-users">(.*?)</span>',first_text)
print('students from re = ', studentsre[0])

studentsbs = BeautifulSoup(first_text,'html.parser').find('span', class_='total-users').text
print('students from bs = ', studentsbs)