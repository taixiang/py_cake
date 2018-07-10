import requests
from bs4 import BeautifulSoup


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
            furniture.append((price, title))

    print(furniture)


def doWithStr(str):

    if "面议" in str:
        print(str)
        return str
    start = str.index("¥")
    end = str.index("/")
    new_str = str[start:end]
    print(new_str)
    return new_str

def sort_list():
    strs = ["6","17/","面","3","2面议","5/"]
    strs.sort()
    print(strs)

# getData()
# doWithStr("\n¥52100.00/套")
sort_list()
