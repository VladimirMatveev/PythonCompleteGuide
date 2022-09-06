from bs4 import BeautifulSoup
import urllib.request
import requests

url = "https://www.pravda.com.ua/news/"
r = requests.get(url)
#print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all('div', class_='article_news_list')
#print(news)
results = []
for article in news:
    time = (article.find('div', class_='article_time').get_text())
    header = (article.find('div', class_='article_header').get_text())
    subheader = (article.find('div', class_='article_subheader').get_text())
    results.append({
        'time': time,
        'header': header,
        'subheader': subheader,
    })

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\nВремя:{item["time"]}\nНазвание: {item["header"]}\n{item["subheader"]}\n\n****************************************************\n')
    i += 1
f.close()