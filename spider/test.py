import matplotlib.pyplot as plt
import itchat
itchat.login()
friends = itchat.get_friends(update=True)
def getSex():

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

    plt.show()

getSex()