from bs4 import BeautifulSoup
import urllib.request

class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('div', class_='article_news_list')
        for article in news:
            time = (article.find('div', class_='article_time').get_text())
            header = (article.find('div', class_='article_header').get_text())
            subheader = (article.find('div', class_='article_subheader').get_text())
            self.results.append({
                'time': time,
                'header': header,
                'subheader': subheader,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(
                    f'Новость № {i}\nВремя:{item["time"]}\nНазвание: {item["header"]}\n{item["subheader"]}\n\n****************************************************\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()