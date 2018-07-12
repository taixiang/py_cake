import requests
from bs4 import BeautifulSoup
import xlsxwriter
from io import BytesIO
from urllib.request import urlopen
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter


def get_data():
    # 定义一个列表存储数据
    furniture = []
    # 用于存放家具名，后续用于词云图制作
    file = open('furniture.txt', 'a', encoding='utf-8')
    # 分页数据获取
    for num in range(1, 9):
        url = "http://www.likoujiaju.com/sell/list-66-%d.html" % num
        response = requests.get(url)
        content = BeautifulSoup(response.content, "lxml")
        # 找到数据所在的div块
        sm_offer = content.find("div", class_="sm-offer")
        lis = sm_offer.ul.find_all("li")
        # 遍历每一条数据
        for li in lis:
            price_span = li.find("span", class_="sm-offer-priceNum")
            price = price_span.get_text()
            title_div = li.find("div", class_="sm-offer-title")
            title = title_div.a.get_text()
            # 写入家具名称
            file.write(title + "\n")
            photo_div = li.find("div", class_="sm-offer-photo")
            photo = photo_div.a.img.get("src")
            # 详情链接
            href = photo_div.a.get("href")
            # 数组里每一项是元祖
            furniture.append((price, title, photo, href))
    # 排序
    furniture.sort(key=take_price, reverse=True)
    create_excel(furniture)


# 传参是列表的每一个元素，这里即元祖
def take_price(enum):
    # 取元祖的第一个参数--价格，处理价格得到数值类型进行比较
    price = enum[0]
    if "面议" in price:  # 面议的话就设为0
        return 0
    start = price.index("¥")
    end = price.index("/")
    new_price = price[start + 1:end]
    return float(new_price)


# 创建excel
def create_excel(furniture):
    # 创建excel表格
    file = xlsxwriter.Workbook("furniture.xlsx")
    # 创建工作表
    sheet = file.add_worksheet()
    # 定义表头
    headers = ["价格", "标题", "图片", "详情链接"]
    # 写表头
    for i, header in enumerate(headers):
        # 第一行为表头
        sheet.write(0, i, header)
    # 设置列宽
    sheet.set_column(0, 0, 24)
    sheet.set_column(1, 1, 54)
    sheet.set_column(2, 2, 34)
    sheet.set_column(3, 3, 40)
    for row in range(len(furniture)):  # 行
        # 设置行高
        sheet.set_row(row + 1, 180)
        for col in range(len(headers)):  # 列
            # col=2是当前列为图片，通过url去读取图片展示
            if col == 2:
                url = furniture[row][col]
                image_data = BytesIO(urlopen(url).read())
                sheet.insert_image(row + 1, 2, url, {"image_data": image_data})
            else:
                sheet.write(row + 1, col, furniture[row][col])
    # 关闭表格
    file.close()


def word_count(filename):
    word_dict = {}
    text = open("{}.txt".format(filename), encoding='utf-8').read()
    word = jieba.cut(text)
    words = ",".join(word)
    all_str = words.replace("\n", "").replace(" ", "").replace("【", "").replace("】", "")
    word_list = all_str.split(",")

    for item in word_list:
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
    val = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    print(val)
    file = open('count.txt', 'a', encoding='utf-8')
    for item in val:
        file.write(item[0] + ' ' + str(item[1]) + '\n')


# 词云
def create_word_cloud(filename):
    text = open("{}.txt".format(filename), encoding='utf-8').read()
    wordlist = jieba.cut(text, cut_all=True)
    wl = " ".join(wordlist)
    print(wl)
    # 设置词云
    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 设置最大显示的词云数
        max_words=2000,
        # 这种字体都在电脑字体中，window在C:\Windows\Fonts\下，mac我选的是/System/Library/Fonts/PingFang.ttc 字体
        font_path='C:\\Windows\\Fonts\\simfang.ttf',
        height=500,
        width=500,
        # 设置字体最大值
        max_font_size=100,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    )
    myword = wc.generate(wl)  # 生成词云
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('furniture.png')  # 把词云保存下


def test():
    test = [1, 4, 6, 7]
    for i in test:
        print("=====")
        print(i)


# get_data()
# create_word_cloud("furniture")
word_count("furniture")
# test()
