from datetime import date


def is_rightdate(y, m, d):
    try:
        date(y, m, d)
    except:
        return False
    else:
        return True


def is_leapyear(y1):
    if (y1 % 4 == 0 and y1 % 100 != 0 or y1 % 400 == 0):
        return True
    else:
        return False


def cal_leapyear(y1, y2):
    count = 0;
    for i in range(y1 + 1, y2):
        if (is_leapyear(i)): count += 1
    return count


def cal_month(y, m, d):
    count = 0  # count代表中间的闰年数
    month = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]  # 2018月份表
    dif = y - 2018
    if (dif > 0):
        count = cal_leapyear(2018, y);
        for i in range(0, 12):
            if (is_leapyear(y) and i >= 2):
                month[i] += 1
            month[i] = (month[i] + dif + count) % 7

    elif (dif < 0):
        dif = -dif
        count = cal_leapyear(y, 2018);
        for i in range(0, 12):
            if (is_leapyear(y) and i <= 1):
                month[i] -= 1
            month[i] = (month[i] - dif - count) % 7
    return month


def cal_week(month, m, d):
    x = (month[m - 1] + d) % 7
    if x == 0: x = 7
    return x


def week(y, m, d):
    if not is_rightdate(y, m, d):
        print("日期不合法")
        exit()
    month = cal_month(y, m, d)
    out = cal_week(month, m, d)

    print(y, "年的月份表：")
    for i in month:
        print(i, end=' ')
    print()

    return out


def ACM():
    y = int(input("请输入年"))
    m = int(input("请输入月"))
    d = int(input("请输入日"))

    out = week(y, m, d)
    print("%d年%d月%d日是周%d" % (y, m, d, out))


if __name__ == "__main__":
    y = 2011
    m = 3
    d = 1

    ACM()

    out = week(y, m, d)
    print("%d年%d月%d日是周%d" % (y, m, d, out))
