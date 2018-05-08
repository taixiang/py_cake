import requests
from selenium import webdriver

def read():
    # response = requests.get('https://juejin.im/post/5ac9c3d06fb9a028dd4e8001')
    # 获取浏览器驱动
    driver = webdriver.Chrome()
    # 浏览器窗口最大化
    # driver.minimize_window()
    # 浏览器地址定向为qq登陆页面
    driver.get("https://juejin.im/post/5ad3fe2d6fb9a028e25e03d7")
    driver.close()


if __name__ == "__main__":
    for i in [1,2,3,4,5,6,7,8,9,10]:
        read()
