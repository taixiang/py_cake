import requests
from bs4 import BeautifulSoup

import os
import django
import time, datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from spider.models import learn


# learnEn = learn.objects.get_or_create(time="12-27")

# time1==最新的
def spiderEn():
    response = requests.get("http://m.chinavoa.com/51voa/")
    soup = BeautifulSoup(response.content, "html5lib")
    content = soup.find("dl", class_="block_con").dd.ul
    lilist = content.find_all("li")

    for index, li in enumerate(lilist):
        if "VOA慢速英语" in li.a.contents[1]:
            time1 = li.a.contents[0].string
            title = li.a.contents[1][8:]
            lLast = learn.objects.first()
            if (lLast == None) or time1 != lLast.time:
                print(11111)
                learnEn = learn()
                learnEn.title = title
                learnEn.time = str(datetime.datetime.now().year) +"-"+time1
                detailRep = requests.get(li.a.get("href"))
                detailSoup = BeautifulSoup(detailRep.content, "html5lib")
                plist = detailSoup.find("div", class_="neirong").find_all("p")
                en_content = ""
                for p in plist:
                    if p.string:
                        en_content = en_content + p.string + "\n"
                learnEn.content = en_content
                learnEn.save()
            else:
                return

spiderEn()