import numpy as np
import sys

'''
0 1 背包问题
问题描述：有N件物品和一个容量为V的背包。第i件物品的费用（即体积，下同）是w[i]，价值是val[i]。
求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
'''


# nn 表示 物品的属性
# c 表示 背包的重量
def knapsack_problem(c):

    # 存储物品的重量
    w = [1, 3, 4, 5, 1]
    # 存储物品的价值
    v = [20, 30, 50, 10, 60]
    # 创建一个二维数组 行数为 物品的个数，列数为背包的重量 从1开始 直至 最大重量
    ll = np.zeros((len(w) + 1, c + 1))

    # 按物品的个数循环
    for i in range(1, ll.shape[0]):
        # 按背包重量循环
        for j in range(1, ll.shape[1]):
            # 当前物品重量小于等于背包的容量
            if w[i-1] <= j:
                # 比较 （当前物品价值+去除该重量后背包里还能容纳重量的价值） 与 （还没有加入该物品时，背包里所达到的最大价值）的大小，取较大的数
                ll[i][j] = int(max(ll[i - 1][j], v[i-1] + ll[i - 1][j - w[i-1]]))

                # 判断是否为第一行
                # if i - 1 < 0:
                #     ll[i][j] = v[i]
                # else:
                #     # 判断是否为第一列
                #     if j - 1 < 0 or j + 1 - w[i] == 0:
                #         # 如果为第一列 此时价值的最大值 则为当前物品的价值 与 上一行 背包里的价值 取 较大的
                #         ll[i][j] = int(max(ll[i-1][j], v[i]))
                #     else:
                #         # 非第一列 则需
                #         ll[i][j] = int(max(ll[i-1][j], v[i] + ll[i-1][j-w[i]]))
            else:
                # 当前物品重量大于背包的容量，则此时背包的价值还为上一次没有该物品的最大价值
                ll[i][j] = ll[i - 1][j]

                # if i == 1 < 0:
                #     # 如果为 第一行则为0
                #     ll[i][j] = 0
                # else:
                #     # 非第一行 则为 上一行的 该背包重量的值
                #     ll[i][j] = ll[i-1][j]
    print(int(ll[len(w)][c]))
    return


# 凑钱问题
def return_money(k):

    # 定义一个数组 用于存储 已经 算完的 硬币的枚数
    aa = [0 for i in range(0, 100)]

    # 判断 当前所求钱数 是否已经 存入数组中
    if aa[k] != 0:
        return aa[k]

    # 零钱 为 1， 3， 5  所以凑该钱数的 硬币枚数为 1
    if k == 1 or k == 3 or k == 5:
        return 1

    if k == 2 or k == 4:
        return 2

    # 所凑钱数 为0时  硬币枚数为 1
    if k <= 0:
        return 0

    # 根据 所拥有的零钱，把钱数划分为3个子结构 分别为 k-1, k-3, k-5
    aa[k] = int(min(return_money(k - 1) + 1, return_money(k - 3) + 1, return_money(k - 5) + 1))

    return aa[k]


# 凑钱问题
def return_money_two(k):
    # 硬币 面值
    nn = [1, 3, 5]
    # 数组初始化 为 最大值
    aa = [sys.maxsize for i in range(1, k)]
    aa[0] = 0
    # 从 1 开始循环 到 所凑钱数
    for i in range(1, k+1):
        # 循环 硬币面值
        for j in range(len(nn)):
            # 判断 存储在数组中的 硬币数 是否为 最小
            if i >= nn[j] and aa[i - nn[j]] + 1 < aa[i]:
                aa[i] = aa[i - nn[j]] + 1
    print(aa[k])
    return


# 最长子序列
def length_list(nn):

    # 数组初始化 为 1
    ll = [1 for k in range(len(nn))]
    # 每次以 第 x 个 元素结尾
    for x in range(0, len(nn)):
        # 循环 以第 p 个元素为结尾的子序列
        for p in range(0, x + 1):
            # 找到 以 p 结尾 并且 小于 x 的 序列  判断前一次 以p结尾序列长度 和本次以p结尾序列长度的 取最大值
            if nn[p] < nn[x]:
                ll[x] = int(max(ll[x], ll[p] + 1))
    return max(ll)


def knapsack_problem(c):
    # 存储物品的重量
    w = [1, 3, 4, 1]
    # 存储物品的价值
    v = [100, 200, 300, 200]
    # 创建一个二维数组 行数为 物品的个数，列数为背包的重量 从1开始 直至 最大重量
    ll = np.zeros((len(w) + 1, c + 1))
    # 按物品的个数循环
    for i in range(1, ll.shape[0]):
        # 按背包重量循环
        for j in range(1, ll.shape[1]):
            # 当前物品重量小于等于背包的容量
            if w[i-1] <= j:
                # 比较 （当前物品价值+去除该重量后背包里还能容纳重量的价值） 与 （还没有加入该物品时，背包里所达到的最大价值）的大小，取较大的数
                ll[i][j] = int(max(ll[i - 1][j], v[i-1] + ll[i - 1][j - w[i-1]]))
            else:
                ll[i][j] = ll[i - 1][j]
    print("装入背包中物品的最大总价值为 %s" % int(ll[len(w)][c]))
    return


if __name__ == '__main__':
    knapsack_problem(4)






