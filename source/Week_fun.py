def is_leapyear(y1):
    if (y1 % 4 == 0 and y1 % 100 != 0 or y1 % 400 == 0):
        return True
    else:
        return False


def cal_month(y):
    delta = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    if is_leapyear(y):
        delta[1] += 1
    month = [0] * 12
    month[0] = week(y, 1, 1)
    for i in range(1, 12):
        month[i] = (month[i - 1] + delta[i - 1]) % 7

    print(y, "年的月份表：")
    for i in month:
        print(i, end=' ')
    print()

    return month


def week(y, m, d):
    c = y // 100
    y = y % 100
    if m <= 2:
        m = m + 12
        y = y - 1
    W = y + int(y / 4) + int(c / 4) - 2 * c + int(26 * (m + 1) / 10) + d - 1
    W = W % 7
    if W == 0:
        W = 7
    return W


def ACM():
    y = int(input("请输入年"))
    m = int(input("请输入月"))
    d = int(input("请输入日"))

    out = week(y, m, d)
    month = cal_month(y)
    print("%d年%d月%d日是周%d" % (y, m, d, out))


if __name__ == "__main__":
    y = 2011
    m = 3
    d = 1

    ACM()

    out = week(y, m, d)
    month = cal_month(y)
    print("%d年%d月%d日是周%d" % (y, m, d, out))
