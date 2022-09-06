from Parser_class import Parser

parser = Parser("https://www.pravda.com.ua/news/", 'news.txt')
parser.run()
# print(parser.raw_html)
# print(parser.html)
#print(parser.results)