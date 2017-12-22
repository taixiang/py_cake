import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from spider.models import article


class testSpide:
    def __init__(self):
        self.startSpider(article())

    def startSpider(self, article):
        response = requests.get('https://meiriyiwen.com/random')
        soup = BeautifulSoup(response.content, "html5lib")
        total = soup.find("div", id="article_show")
        title = total.h1.string
        author = total.find("p", class_="article_author").string
        print(title)
        article.title = title
        article.author = author
        contents = total.find("div", class_="article_text").find_all("p")
        art_content = ""
        for content in contents:
            art_content = art_content + content.string
        print(art_content)
        article.content = art_content
        article.save()


testSpide()
