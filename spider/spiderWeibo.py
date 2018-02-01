# coding:utf-8

import time
from selenium import webdriver
from lxml import etree
import importlib

# 这里一定要设置编码格式，防止后面写入文件时报错



friend = ''  # 朋友的QQ号，朋友的空间要求允许你能访问
user = '467220125@qq.com'  # 你的QQ号
pw = ''  # 你的QQ密码

# 获取浏览器驱动
driver = webdriver.Chrome()

# 浏览器窗口最大化
driver.maximize_window()

# 浏览器地址定向为登陆页面
driver.get("https://weibo.com/")

time.sleep(8)

# 账号输入框输入已知账号
driver.find_element_by_name("username").send_keys(user)

# 密码框输入已知密码
driver.find_element_by_name("password").send_keys(pw)

# 自动点击登陆按钮
driver.find_element_by_class_name("W_btn_a").click()

# 让webdriver操纵当前页
driver.switch_to.default_content()

# 跳到说说的url, friend你可以任意改成你想访问的空间
driver.get("https://weibo.com/esportsht?profile_ftype=1&is_all=1#_0")

next_num = 0  # 初始“下一页”的id
while True:

    # 下拉滚动条，使浏览器加载出动态加载的内容，
    # 我这里是从1开始到6结束 分5 次加载完每页数据
    for i in range(1, 6):
        height = 20000 * i  # 每次滑动20000像素
        strWord = "window.scrollBy(0," + str(height) + ")"
        driver.execute_script(strWord)
        time.sleep(4)

    # 很多时候网页由多个<frame>或<iframe>组成，webdriver默认定位的是最外层的frame，
    # 所以这里需要选中一下说说所在的frame，否则找不到下面需要的网页元素
    # driver.switch_to.frame("app_canvas_frame")
    selector = etree.HTML(driver.page_source)
    name = selector.xpath('//h1[@class="username"]/text()')
    divs = selector.xpath('//div[@class="WB_feed WB_feed_v3 WB_feed_v4"]/div')

    print(divs[1].xpath('.//div[@class="WB_feed_detail clearfix"]')[0].xpath('./div')[2])

    # 这里使用 a 表示内容可以连续不清空写入
    with open('sina_haitao_word.txt', 'a', encoding='utf-8') as f:
        for div in range(1, len(divs) - 1):
            sina_div = divs[div].xpath('.//div[@class="WB_feed_detail clearfix"]')[0].xpath('./div')[2]
            sina_name = sina_div.xpath('./div')[0].xpath('./a/text()')[0]
            sina_content = sina_div.xpath('./div')[2].xpath('./text()')[0].strip()
            sina_time = sina_div.xpath('./div')[1].xpath('./a')[0].xpath('./text()')[0]
            print(sina_time, sina_content)
            if '2017' in sina_time:
                break
            f.write(sina_content+"\n")

    # # 当已经到了尾页，“下一页”这个按钮就没有id了，可以结束了
    if driver.page_source.find('page next S_txt1 S_line1') == -1:
        break
    #
    # # 找到“下一页”的按钮，因为下一页的按钮是动态变化的，这里需要动态记录一下
    driver.find_element_by_class_name('next').click()

    #
    # # “下一页”的id
    next_num += 1
    #
    # # 因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
    # driver.switch_to.parent_frame()
