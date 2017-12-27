import requests
from bs4 import BeautifulSoup

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from spider.models import learn

learnEn = learn.objects.get_or_create(time="12-27")




response = requests.get("http://m.chinavoa.com/51voa/")
soup = BeautifulSoup(response.content, "html5lib")
content = soup.find("dl", class_="block_con").dd.ul
lilist = content.find_all("li")

detailRep = requests.get(lilist[0].a.get("href"))
detailSoup = BeautifulSoup(detailRep.content, "html5lib")
plist = detailSoup.find("div", class_="neirong").find_all("p")
for p in plist:
    if p.string:
        print(p.string)

# for li in lilist:
#     if "VOA慢速英语" in li.a.contents[1]:
#         url2 = requests.get(li.a.get("href"))
#         print(url2)
#         print(li.a.contents[0].string)
#         print(li.a.contents[1])
#         print(li.a.get("href") + "\n")
