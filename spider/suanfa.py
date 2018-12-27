def deleteSameNum(num):
    num.sort()
    last = num[-1]
    for i in range(len(num) - 2, -1, -1):
        if last == num[i]:
            del num[i]
        else:
            last = num[i]
    return num


def test():
    nums = [-1, 0, 1, 2, -1, -4]
    total_list = []
    for i in nums:
        for j in nums:
            for k in nums:
                total = i + j + k
                if total == 0:
                    item_list = [i, j, k]
                    total_list.append(item_list)

    t = deleteSameNum(total_list)
    print(t)

test()
