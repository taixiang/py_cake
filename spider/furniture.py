import requests
from bs4 import BeautifulSoup
import xlsxwriter
from io import BytesIO
from urllib.request import urlopen


def takeSort(elem):
    return elem[2]


def test_list(furniture):
    file = xlsxwriter.Workbook("test.xlsx")
    sheet = file.add_worksheet()

    headers = ["价格", "标题"]
    # 写表头
    for i, header in enumerate(headers):
        sheet.write(0, i, header)
    # sheet.write(0, 1, "test text")
    # file.save("test.xls")
    t = [('\n¥52100.00/套 ', '【合和木缘】家具黑胡桃简约现代客厅沙发可定制GY-HW02'), ('\n¥20180.00/件 ', '高端实木沙发组合单人双人三人位现代中式客厅家具胡桃木'),
         ('\n¥13800.00/件 ', '胡桃木沙发布艺实木沙发纯实木沙发中式木架沙发L型转角'), ('\n¥13260.00/组 ', '【合和木缘】俄罗斯榆木北欧简约实木沙发组合GY-YW08'),
         ('\n¥15300.00/件 ', '【合和木缘】俄罗斯榆木北欧简约实木沙发组合GY-YW09'), ('\n¥16680.00/套 ', '实木布艺沙发 新中式客厅沙发组合 简约实木沙发'),
         ('\n¥24000.00/件 ', '【合和木缘】家具黑胡桃简约现代客厅沙发可定制GY-HW05'), ('\n¥29240.00/件 ', '【合和木缘】家具黑胡桃简约现代客厅沙发可定制GY-HW01'),
         ('\n¥49700.00/套 ', '【合和木缘】家具黑胡桃简约现代客厅沙发可定制GY-HW04'), ('\n¥35700.00/套 ', '【合和木缘】家具黑胡桃简约现代客厅沙发可定制GY-HW07'),
         ('\n¥331900.00/套（3+1+1） ', '【合和木缘】俄罗斯榆木北欧简约沙发组合GY-YW07'), ('\n¥22200.00/套 ', '【合和木缘】俄罗斯榆木北欧简约转角沙发GY-YW05'),
         ('\n¥10700.00/件 ', '【合和木缘】俄罗斯榆木北欧简约转角沙发GY-YW04'), ('\n¥13900.00/件 ', '【合和木缘】俄罗斯榆木北欧简约转角沙发GY-YW01'),
         ('\n¥22200.00/套（3+1+1） ', '【合和木缘】俄罗斯榆木北欧简约转角沙发GY-YW06'), ('\n¥6560.00/件 ', '【合和木缘】北欧白橡木家具转角沙发GY-XS4'),
         ('\n¥2336.00/件 ', '白橡木系列木蜡油高端环保家具沙发电视柜茶几GY-BX01'), ('\n¥9600.00/套(321) ', '【合和木缘】高端地中海系列白蜡木家具沙发组合GY-DW06'),
         ('\n¥8800.00/件（带小柜） ', '【合和木缘】高端地中海系列白蜡木家具转角沙发GY-DW08'),
         ('\n¥9990.00/套(321) ', '【合和木缘】高端地中海系列白蜡木家具沙发组合GY-DW08'), ('\n¥7410.00/套 ', '【合和木缘】地中海全松木家具沙发组合GY-SW301'),
         ('\n¥1200.00/件 ', '【合和木缘】北欧白橡木家具客厅家具双人丹麦沙发GY-XS2'), ('\n¥面议 ', '【合和木缘】美式家具工厂直销'),
         ('\n¥12944.00/套 ', '【合和木缘】黄金海棠木纯实木家具转角沙发GY-D913'), ('\n¥12944.00/套 ', '【合和木缘】黄金海棠木纯实木家具转角沙发GY-D911'),
         ('\n¥20128.00/套 ', '【合和木缘】黄金海棠木纯实木家具沙发组合GY-D910'), ('\n¥16064.00/套 ', '【合和木缘】黄金海棠木纯实木家具沙发组合GY-D909'),
         ('\n¥23072.00/套 ', '【合和木缘】黄金海棠木纯实木家具沙发GY-D912'), ('\n¥14400.00/套 ', '【合和木缘】北欧简约俄罗斯水曲柳实木转角沙发GY-QW02'),
         ('\n¥7360.00/件 ', '【合和木缘】北欧简约俄罗斯水曲柳实木转角沙发GY-QW01')]
    sheet.set_column(1, 1, 50)
    for i, f in enumerate(furniture):  # 行
        if i == 0:
            sheet.set_row(1, 150)
            print("===============")
            url = "http://v2.kaoyango.com/static/web/img/index/in1-1h.png"
            image_data = BytesIO(urlopen(url).read())
            sheet.insert_image(1, 2, url, {"image_data": image_data})
        for j, h in enumerate(headers):  # 列
            # if j == 1:
            #     sheet.set_column(j, j + 1, 100)
            sheet.write(i + 1, j, furniture[i][j])
    file.close()


def getData():
    furniture = []
    for num in range(1, 2):
        url = "http://www.likoujiaju.com/sell/list-66-%d.html" % num
        response = requests.get(url)
        content = BeautifulSoup(response.content, "lxml")
        sm_offer = content.find("div", class_="sm-offer")
        lis = sm_offer.ul.find_all("li")

        for li in lis:
            price_span = li.find("span", class_="sm-offer-priceNum")
            price = price_span.get_text()
            title_div = li.find("div", class_="sm-offer-title")
            title = title_div.a.get_text()
            furniture.append((price, title, split_price(price)))

    furniture.sort(key=takeSort)
    test_list(furniture)
    print(furniture)


# 处理价格，便于通过价格筛选
def split_price(price):
    if "面议" in price:
        return 0
    start = price.index("¥")
    end = price.index("/")
    new_price = price[start + 1:end]
    return float(new_price)


def sort_list():
    strs = [("2222", "", 2), ("333", "", 3), ("111", "", 1)]
    strs.sort(key=takeSort)
    print(strs)


def write_img():
    test_book = xlsxwriter.Workbook("test.xls")
    sheet = test_book.add_worksheet()
    # sheet.insert_image(0, 0, "1111.jpg")
    # test_book.close()
    url = "http://v2.kaoyango.com/static/web/img/index/in1-1h.png"
    image_data = BytesIO(urlopen(url).read())
    sheet.insert_image(0, 0, url, {"image_data": image_data})
    test_book.close()


# test_list()
getData()
# doWithStr("\n¥52100.00/套")
# sort_list()
# write_img()
