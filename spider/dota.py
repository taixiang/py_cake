import requests, json
import matplotlib.pyplot as plt


def bp(item, bp_key, bp_dict):
    for bp in item[bp_key]:
        key = bp["name"]
        if key in bp_dict.keys():
            bp_dict[key]["count"] = bp_dict[key]["count"] + 1
        else:
            bp.update(count=1)
            bp_dict[key] = bp
    return bp_dict


def dota():
    b_dict = dict()
    p_dict = dict()
    b_win_dict = dict()
    p_win_dict = dict()
    page = 1
    while True:
        url = "https://www.dotamore.com/api/v1/league/matchlist?league_id=9870&page=%d&size=12" % page
        response = requests.get(url)
        data = json.loads(response.text)
        page += 1
        for item in data["data"]:
            if item["end_time"] < "2018-08-19 08:18":
                # x[0]是根据键排序，x[1]是根据值，这里的值是字典，取["count"]项排序，得到的是元祖的list
                new_b_dict = sorted(b_dict.items(), key=lambda x: x[1]["count"], reverse=True)
                for i, hero in enumerate(new_b_dict):
                    count = hero[1]["count"]
                    print(hero[1]["name_cn"] + "   " + str(hero[1]["count"]))
                    plt.bar(hero[1]["name_cn"], hero[1]["count"])
                plt.show()
                print(b_dict)
                print(new_b_dict)
                print(p_dict)
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


dota()
