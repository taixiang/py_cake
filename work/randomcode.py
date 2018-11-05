from PIL import Image, ImageDraw, ImageFont
import random


# 生成随机颜色
def getRandomColor():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)


def getRandomStr():
    random_num = str(random.randint(0, 9))
    random_lower = chr(random.randint(97, 122))  # 数字转ascii码
    random_upper = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_lower, random_upper])
    return random_char


def createImg():
    img = Image.new(mode="RGB", size=(150, 40), color=getRandomColor())
    img = img.convert("RGBA")
    img.putalpha(205)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font="arial.ttf", size=28)
    for i in range(5):
        random_item = getRandomStr()
        print(random_item)
        draw.text((10 + 18 * i, 0), text=random_item, fill=getRandomColor(), font=font)
    with open("pic.png", "wb") as f:
        img.save(f, format="png")


createImg()
