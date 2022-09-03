from bs4 import BeautifulSoup
import urllib.request
import requests

url = "https://www.pravda.com.ua/news/"
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all('div', class_='article_news_list')
print(news)
for article in news:
    print(article.find('div', class_='article_time').get_text())

#print(soup.find('div', class_='article_time').find('div', class_='article_header'))
#article_time  article_content
