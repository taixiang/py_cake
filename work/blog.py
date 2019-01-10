# coding:utf-8
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import jieba

def file(root):
    total = ""
    file_list = os.listdir(root)
    for file in file_list:
        path = os.path.join(root,file)
        text = open(path, encoding='utf-8').read()
        total = total + "\n" + text

    # rec = re.compile("[^\u4E00-\u9FA5]")
    # total = rec.sub("", total)
    wordlist = jieba.cut(total, cut_all=True)
    wl = " ".join(wordlist)
    # wl = "1111 qqq 中国"
    print(wl)

    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 设置最大显示的词云数
        max_words=1000,
        # 这种字体都在电脑字体中，window在C:\Windows\Fonts\下，mac下的是/System/Library/Fonts/PingFang.ttc 字体
        font_path='C:\\Windows\\Fonts\\STFANGSO.ttf',
        height=4000,
        width=4000,
        # 设置字体最大值
        max_font_size=250,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    )
    myword = wc.generate(wl)  # 生成词云
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.savefig("getsex.png")  # 保存图片
    plt.ion()
    plt.pause(5)
    plt.close()  # 图片显示5s，之后关闭
    # plt.show()
    # wc.to_file('blog.png')  # 把词云保存下

def word(filename):
    text = open(filename, encoding='utf-8').read()
    print(text)

# word("F:\新建文件夹\md\关于我.md")
file("F:\新建文件夹\md")