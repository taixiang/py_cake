import requests
import time, datetime
import json, threading
import webbrowser
import urllib.parse
from django.core import serializers
from spider import methods


#
def getData():
    # http://www.mocky.io/v2/5a56c7242e0000d70411fead  http://htpmsg.jiecaojingxuan.com/msg/current  http://www.mocky.io/v2/5a56f5df2e0000690e11ff1f
    count = 0
    while True:
        time.sleep(0.5)
        resptext = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current', timeout=5)
        if resptext.status_code == 200:
            result = json.loads(resptext.text)
            print(result)
            if "data" in result.keys() and "correctOption" not in result["data"]["event"].keys() and count < 1:
                question = result["data"]["event"]["desc"].split(".")[1]
                choices = result["data"]["event"]["options"].strip("[").strip("]").replace('"', "").split(",")
                print(choices)
                count += 1
                t1 = threading.Thread(methods.run_algorithm(0, question, choices))
                t2 = threading.Thread(methods.run_algorithm(1, question, choices))
                t3 = threading.Thread(methods.run_algorithm(2, question, choices))
                t1.start()
                t2.start()
                t3.start()
            elif "data" not in result.keys():
                count = 0
            f = open("./cddh3", "a")
            f.write(resptext.text + "\n")
            f.close()



if __name__ == "__main__":
    # getData()
    getData()

    # def getData():
    #     result = urllib.parse.quote("“白寿”在中国古代指的是多少岁")
    #     webbrowser.open('https://baidu.com/s?wd='+result)
    #
    # getData()
