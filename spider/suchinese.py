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
        # for num in range(3742, 3794):
            response = requests.get('https://yuwen.chazidian.com/kewen3851/')
            soup = BeautifulSoup(response.content, "html5lib")
            yuList = soup.find("div", class_="kewen_list")
            liList = yuList.ul.find_all("li")
            for li in liList:
                print(li.a.get("href"))
                print(li.string)
                response2 = requests.get(li.a.get("href"))
                soup2 = BeautifulSoup(response2.content, "html5lib")
                left = soup2.find("div", class_="showjj_left")
                detail = requests.get(left.p.a.get("href"))
                detail2 = BeautifulSoup(detail.content, "html5lib")
                content = detail2.find("div", class_="jiathis_streak")
                text = content.get_text().strip().replace("\n", "")
                print(text)
                f = open("./su9down", "a")
                f.write(li.string + "\n")
                f.write(text+"\n")
                f.close()


testSpide()
