import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
# from spider.models import article


class testSpide:
    def __init__(self):
        self.startSpider()

    def startSpider(self):
        for num in range(483, 507)[::-1]:
            response = requests.get('http://www.yuwenziyuan.com/rjb/zhuanti/'+str(num)+'/')
            soup = BeautifulSoup(response.content, "html5lib")
            softName = soup.find("span", class_="mainSoftName")
            print(softName.a.get("href"))
            print(softName.string)

            response2 = requests.get("http://www.yuwenziyuan.com"+softName.a.get("href"))
            soup2 = BeautifulSoup(response2.content, "html5lib")
            content = soup2.find("div", class_="ckqw")
            text = content.get_text().lstrip()
            print(text)

            f = open("./9down", "a")
            f.write(softName.string+"\n")
            f.write(text)
            f.close()

        # title = total.h1.string
        # author = total.find("p", class_="article_author").string
        # print(title)
        # contents = total.find("div", class_="article_text").find_all("p")
        # art_content = ""
        # for content in contents:
        #     art_content = art_content + content.string
        # print(art_content)
        #
        # f = open("./1112.doc","w")
        # f.write(art_content)
        # f.close()
        # # article.save()


testSpide()
