import requests
from bs4 import BeautifulSoup

import os
import django
import time, datetime
import json, threading
import webbrowser
import urllib.parse

#
# def getData():
#     resptext = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current', timeout=5).text
#     resptext_dict = json.loads(resptext)
#     print(resptext_dict)
#     # f = open("./cddh", "a")
#     # f.write(resptext + "\n")
#     # f.close()
#     global timer
#     timer = threading.Timer(1.0, getData)
#     timer.start()
#
#
# if __name__ == "__main__":
#     timer = threading.Timer(1.0, getData)
#     timer.start()

def getData():
    result = urllib.parse.quote("“白寿”在中国古代指的是多少岁")
    webbrowser.open('https://baidu.com/s?wd='+result)

getData()