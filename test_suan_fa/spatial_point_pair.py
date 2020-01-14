import random
import math
import sys


# 一维空间点对
def one_dimensional(n):
    # 生成 列表
    nn = random_list(n)
    # 列表排序
    nn = bubble_sort(nn)
    print(nn)

    return one_dimensional_part(nn, 0, len(nn), nn)


#
def one_dimensional_part(nn, i, j, mm):
    # 当集合中元素个数 小于 2 时
    if len(nn) < 2:
        return sys.maxsize
    # 当集合中元素个数 等于 2 时
    if len(nn) == 2:
        return int(math.fabs(nn[0] - nn[1])) if int(math.fabs(nn[0] - nn[1])) > 0 else sys.maxsize

    # 中间位置
    k = int(len(nn)/2)
    # 左集合
    left = mm[i:k + i + 1]
    # 右集合
    right = mm[k + i + 1:j + i + 1]

    # 左集合 距离
    d1 = one_dimensional_part(left, i, k, mm)
    # 右集合 距离
    d2 = one_dimensional_part(right, k + 1, j, mm)

    # 左集合 最大值
    kk = max(left)
    # 右集合 最小值
    ll = min(right)

    return min(d1, d2, int(math.fabs(kk - ll)) if int(math.fabs(kk - ll)) > 0 else sys.maxsize)


# 二维空间点对
def two_dimensional(n):
    # 定义一个空列表
    ll = []
    # 生成n个二维坐标
    for i in range(n):
        n = random.randrange(1, 10)
        m = random.randrange(5, 15)
        kk = [n, m]
        ll.append(kk)

    # 对二维坐标以 x轴排序
    ll = [[2, 2], [1.5, 1.5], [3.5, 1], [1.75, 1.25]]
    nn = bubble_sort_two_x(ll)
    print(ll)

    return two_dimensional_part(nn, nn, 0, len(nn)) ** 0.5


#
def two_dimensional_part(nn, mm, i, j):
    # 当集合中元素个数 小于 2 时
    if len(nn) < 2:
        return sys.maxsize
    # 当集合中元素个数 等于 2 时
    if len(nn) == 2:
        if (nn[0][0] - nn[1][0]) ** 2 + (nn[0][1] - nn[1][1]) ** 2 > 0:
            return (nn[0][0] - nn[1][0]) ** 2 + (nn[0][1] - nn[1][1]) ** 2
        else:
            return sys.maxsize

    # TODO 考虑 三个点的时候

    # 中间位置
    k = int(len(nn)/2)
    # 中间位置x坐标
    x_mid = nn[k][0]

    # 左集合
    left = mm[i:k + i + 1]
    # 右集合
    right = mm[k + i + 1:j + i + 1]

    # 左集合 距离
    d1 = two_dimensional_part(left, mm, i, k)
    # 右集合 距离
    d2 = two_dimensional_part(right, mm, k + 1, j)

    # 找出 左右 集合 中 距离的最小值
    dd = min(d1, d2)

    gg = []
    # 找出 左集合到 中间点 距离 小于 d 的 坐标
    for i in range(len(left)):
        if math.fabs(left[i][0] - x_mid) <= dd:
            gg.append(left[i])
    # 找出 右集合 到中间点 距离 小于 d 的 坐标
    for i in range(len(right)):
        if math.fabs(right[i][0] - x_mid) <= dd:
            gg.append(right[i])

    # 对二维坐标  以y轴排序
    gg = bubble_sort_two_y(gg)

    # TODO 从左集合 或者 右集合 选出的坐标为空时

    # 最小距离 初始化为 dd
    min_distance = dd
    # 计算 左集合，右集合，和两个集合交叉的最小值
    for i in range(0, k + 1):
        for j in range(k+1, len(gg)):
            # 比较超过 6个 则退出
            if j - k - 1 > 6:
                break
            # 如果 左集合 点的y 坐标 与 右集合 点 y坐标 相差 大于 最小距离 dd 则退出
            if gg[j][1] - gg[i][1] > dd:
                break
            # 计算 两点间距离
            dd_mid = (gg[i][0] - gg[j][0]) ** 2 + (gg[i][1] - gg[j][1]) ** 2 \
                if (gg[i][0] - gg[j][0]) ** 2 + (gg[i][1] - gg[j][1]) ** 2 > 0 else sys.maxsize
            # 找出 每次 循环的最小值
            min_distance = min(min_distance, dd_mid)

    return min_distance


# 对二维坐标 以 x 轴排序
def bubble_sort_two_x(nn):
    for i in range(len(nn)):
        for j in range(len(nn) - 1):
            if nn[j][0] > nn[j + 1][0]:
                temp = nn[j]
                nn[j] = nn[j + 1]
                nn[j + 1] = temp
    return nn


# 对二维坐标 以 y 轴排序
def bubble_sort_two_y(nn):
    for i in range(len(nn)):
        for j in range(len(nn) - 1):
            if nn[j][1] > nn[j + 1][1]:
                temp = nn[j]
                nn[j] = nn[j + 1]
                nn[j + 1] = temp
    return nn


# 冒泡排序
def bubble_sort(nn):
    for i in range(len(nn)):
        for j in range(len(nn) - 1):
            if nn[j] > nn[j + 1]:
                temp = nn[j]
                nn[j] = nn[j + 1]
                nn[j + 1] = temp
    return nn


# 随机生成N个数的list
def random_list(n):
    # 生成一个空的 list
    nn = []
    while n > 0:
        # 生成 100 以内的随机数
        cc = random.randrange(100)
        nn.append(cc)
        n -= 1
    return nn


if __name__ == '__main__':
    # print(one_dimensional(10))
        print(two_dimensional(20))
    # nn = [[1.5, 1.5], [1.75, 1.25]]
    # print((nn[0][0] - nn[1][0]) ** 2 + (nn[0][1] - nn[1][1]) ** 2)


