# coding:utf-8
import requests
import itchat
import os
import math
import PIL.Image as Image
import matplotlib.pyplot as plt
import random
from matplotlib.font_manager import FontManager, FontProperties

font = FontProperties(fname='/Library/Fonts/Songti.ttc')


# get_friends
#
# itchat.get_friends() 返回完整的好友列表
# 每个好友为一个字典, 其中第一项为本人的账号信息;
# 传入 update=True, 将更新好友列表并返回, get_friends(update=True)

def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


def getFriends():
    itchat.login()
    friends = itchat.get_friends(update=True)
    # itchat.get_head_img() 获取到头像二进制，并写入文件，保存每张头像
    for count, f in enumerate(friends):
        img = itchat.get_head_img(userName=f["UserName"])
        imgFile = open("img/" + str(count) + ".jpg", "wb")
        imgFile.write(img)
        imgFile.close()


def createImg():
    x = 0
    y = 0
    imgs = os.listdir("img")
    random.shuffle(imgs)
    # 创建640*640的图片用于填充各小图片
    newImg = Image.new('RGBA', (640, 640))
    # 以640*640来拼接图片，math.sqrt()开平方根计算每张小图片的宽高，
    width = int(math.sqrt(640 * 640 / len(imgs)))
    # 每行图片数
    numLine = int(640 / width)

    for i in imgs:
        print(i)
        img = Image.open("img/" + i)
        # 缩小图片
        img = img.resize((width, width), Image.ANTIALIAS)
        # 拼接图片，一行排满，换行拼接
        # newImg.paste(img, (x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
            # newImg.save("all1.png")


def getSex():
    itchat.login()
    friends = itchat.get_friends(update=True)
    sex = dict()
    for f in friends:
        if f["Sex"] == 1:
            sex["man"] = sex.get("man", 0) + 1
        elif f["Sex"] == 2:
            sex["women"] = sex.get("women", 0) + 1
        else:
            sex["unknown"] = sex.get("unknown", 0) + 1
    print(sex)
    for i, key in enumerate(sex):
        plt.bar(key, sex[key])
    plt.title(u"性别分布图", fontproperties=font)
    plt.show()


getSex()
# getFriends()
# createImg()
