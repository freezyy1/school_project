# для корректного отображения новостей перепишите парсер под сайт своей школы
import requests
from bs4 import BeautifulSoup
from tokens import url_school
url = url_school
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all('h2', class_='item-page-title')
news_list = ['Актуальные новости:']
for quote in links:
    news_list.append(quote.text)

news_list = "\n".join(news_list)
