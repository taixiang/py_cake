import requests, json
from io import BytesIO
from urllib.request import urlopen
import xlsxwriter


# item 指radiant 或dire 项，bp_key指radiant 或dire  里的bans、picks数据
def bp(item, bp_key, bp_dict):
    # 遍历bans 或picks 数据
    for bp in item[bp_key]:
        key = bp["name"]
        # 如果这个英雄已存在，count+1
        if key in bp_dict.keys():
            bp_dict[key]["count"] = bp_dict[key]["count"] + 1
        else:  # 不存在就记录一条数据
            bp.update(count=1)
            bp_dict[key] = bp
    return bp_dict


def bp2(item, bp_key, bp_dict):
    for bp in item[bp_key]:
        key = bp["name"]
        if bp_key == "bans":
            if key in bp_dict.keys():
                bp_dict[key]["count"] = bp_dict[key]["count"] + 1
                bp_dict[key]["b_count"] = bp_dict[key]["b_count"] + 1
            else:  # 不存在就记录一条数据
                bp.update(count=1)
                bp.update(b_count=1)
                bp_dict[key] = bp


def dota():
    b_dict = dict()
    p_dict = dict()
    b_win_dict = dict()
    p_win_dict = dict()
    page = 1
    while True:
        url = "https://www.dotamore.com/api/v1/league/matchlist?league_id=9870&page=%d&size=2" % page
        response = requests.get(url)
        data = json.loads(response.text)
        page += 1
        for item in data["data"]:
            if item["end_time"] < "2018-08-19 08:18":
                # x[0]是根据键排序，x[1]是根据值，这里的值是字典，取["count"]项排序，得到的是元祖的list
                new_b_list = sorted(b_dict.items(), key=lambda x: x[1]["count"], reverse=True)
                new_p_list = sorted(p_dict.items(), key=lambda x: x[1]["count"], reverse=True)
                print(new_b_list)
                create_excel(new_b_list, new_p_list)
                return
            bp(item["radiant"], "bans", b_dict)
            bp(item["radiant"], "picks", p_dict)
            bp(item["dire"], "bans", b_dict)
            bp(item["dire"], "picks", p_dict)

            if item["radiant_win"] == 0:
                if item["dire"]["team_id"] == "726228":
                    bp(item["dire"], "bans", b_win_dict)
                    bp(item["dire"], "picks", p_win_dict)
            else:
                if item["radiant"]["team_id"] == "726228":
                    bp(item["radiant"], "bans", b_win_dict)
                    bp(item["radiant"], "picks", p_win_dict)
        print(b_dict)


def create_excel(b_list, p_dict):
    # 创建excel表格
    file = xlsxwriter.Workbook("dota.xlsx")
    # 创建工作表1
    sheet1 = file.add_worksheet("sheet1")
    headers = ["", "英雄", "ban", "", "", "英雄", "pick"]
    # 写表头
    for i, header in enumerate(headers):
        # 第一行为表头
        sheet1.write(0, i, header)

    # ban
    for row in range(len(b_list)):  # 行
        # 设置行高
        sheet1.set_row(row + 1, 60)
        for col in range(len(headers)):  # 列
            if col == 0:
                url = "http://cdn.dotamore.com/heros_id_62_35/%d.png" % b_list[row][1]["id"]
                image_data = BytesIO(urlopen(url).read())
                sheet1.insert_image(row + 1, col, url, {"image_data": image_data})
            if col == 1:
                name = b_list[row][1]["name_cn"]
                sheet1.write(row + 1, col, name)
            if col == 2:
                count = b_list[row][1]["count"]
                sheet1.write(row + 1, col, count)

    # pick
    for row in range(len(p_dict)):  # 行
        # 设置行高
        sheet1.set_row(row + 1, 60)
        for col in range(len(headers)):  # 列
            if col == 4:
                url = "http://cdn.dotamore.com/heros_id_62_35/%d.png" % p_dict[row][1]["id"]
                image_data = BytesIO(urlopen(url).read())
                sheet1.insert_image(row + 1, col, url, {"image_data": image_data})
            if col == 5:
                name = p_dict[row][1]["name_cn"]
                sheet1.write(row + 1, col, name)
            if col == 6:
                count = p_dict[row][1]["count"]
                sheet1.write(row + 1, col, count)
    # 关闭表格
    file.close()


dota()
