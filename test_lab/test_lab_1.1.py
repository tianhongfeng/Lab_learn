import random
import math
#  初级 1.1


# 随机生成N个数的list
def random_list(n):
    # 生成一个空的 list
    nn = []
    for i in range(n):
        # 生成 100 以内的随机数
        cc = random.randrange(100)
        nn.append(cc)
    return nn


# 1.输入整数N，随机生成N个数的list，写一个函数，返回list中最大的数

def function1(n):
    # 调用方法 生成n个数的list
    nn = function1(n)
    # 用于存储 list 中最大的数
    m = 0
    for i in range(len(nn)):
        # 比较大小
        if m < nn[i]:
            m = nn[i]
    return m


# 2.1建立一个空的list，借助空链表的辅助空间，实现题1中所建list的逆转
def function2_1(n):
    # 创建一个 空list 用于辅助空间
    mm = []
    # 调用方法 生成n个数的list
    nn = function1(n)
    # 获取 nn 的长度
    nl = len(nn)
    # 遍历 原来的list
    for i in range(nl):
        mm.append(nn[-(i+1)])
    nn = mm
    return nn


# 2.2用循环遍历和递归遍历两种方法，将题1中的list原地逆转（注：原地逆转是指不借助辅助空间将list逆转）
def function2_2(n):
    # 调用方法 生成n个数的list
    nn = random_list(n)

    # 循环遍历
    mm = literate(nn)
    print(mm)

    # 递归遍历
    i = 0
    nl = len(nn)
    kk = recursion(nn, i, nl)
    print(kk[0])
    return



'''
算法实现原理: 不借助 第三个变量实现 两个数的位置的调换
a = a + b
b = a - b
a = a - b
'''
# 循环遍历 实现 list 逆转
def literate(nn):
    # 计算 list 的长度
    nl = len(nn)
    for i in range(int(nl/2)-1):
        nn[i] = nn[i] + nn[nl-1-i]
        nn[nl-1-i] = nn[i] - nn[nl-1-i]
        nn[i] = nn[i] - nn[nl-1-i]
    return nn


# 递归遍历实现 list 逆转
def recursion(nn, i, nl):
    # 递归 出口
    if i <= int(nl/2)-1:
        nn[i] = nn[i] + nn[nl - 1 - i]
        nn[nl - 1 - i] = nn[i] - nn[nl - 1 - i]
        nn[i] = nn[i] - nn[nl - 1 - i]
        i += 1
        recursion(nn, i, nl)
    return nn, i, nl


# 3.写个函数检查指定的元素是否出现在题1的list中
def function3(n, m):
    # 调用方法 生成n个数的list
    nn = random_list(n)
    # 标记 是否存在指定元素
    kk = False
    for i in range(len(nn)):
        if m == nn[i]:
            kk = True
            break
    if kk is True:
        print("指定数字存在列表中")
    else:
        print("指定数字不存在列表中")
    return


# 4.写个函数返回题1 list中奇数位置的所有元素
def function4(n):
    # 调用方法 生成n个数的list
    nn = random_list(n)
    # 创建一个 存储奇数位置所有元素的list
    mm = []
    i = 0
    while i < len(nn):
        mm.append(nn[i])
        i += 2
    return mm


# 5.写三个函数来计算题1 list中数字的和：分别用for循环，while循环和递归完成。
def function5(n):
    # 调用方法 生成n个数的list
    nn = random_list(n)
    print(nn)
    # for 循环
    print(sum_for(nn))
    # while循环
    print(sum_while(nn))
    # 递归
    i = 0
    sum_list = 0
    print(sum_recursion(nn, i, sum_list)[2])
    return


# for 循环实现 list中数字的和
def sum_for(nn):
    sum_list = 0
    for i in range(len(nn)):
        sum_list += nn[i]
    return sum_list


# while 循环实现 list中数字的和
def sum_while(nn):
    i = 0
    sum_list = 0
    while i < len(nn):
        sum_list += nn[i]
        i += 1
    return sum_list


# 递归 实现 list中数字的和
def sum_recursion(nn, i, sum_list):
    if i < len(nn):
        sum_list += nn[i]
        i += 1
        sum_list = sum_recursion(nn, i, sum_list)[2]
    return nn, i, sum_list,


# 6.写个函数on_all遍历列表中的每个元素，打印出开始的20个完全平方数。
def function6(n):
    # 调用方法 生成n个数的list
    nn = random_list(n)
    for i in range(len(nn)):
        k = int(math.sqrt(nn[i]))
        m = k ** 2
        if m == nn[i]:
            print(nn[i])
    return


# 7.随机生成一个list，对该list使用下面的排序算法进行排序：
# TODO 直接插入排序、希尔排序、简单选择排序、堆排序、冒泡排序、快速排序、归并排序、奇偶排序、臭皮匠排序
def function7(n):
    # 调用方法 生成n个数的list
    nn = random_list(n)
    print(nn)
    # 冒泡排序
    # print(bubble_sort(nn))
    # 直接插入排序
    #print(insert_sort(nn))
    # 简单选择排序
    #print(simple_select_sort(nn))
    # 希尔排序
    # print(shell_sort(nn))
    # 堆排序
    # print(heap_sort(nn))
    # 快速排序
    # print(quick_sort(nn))
    # 归并排序
    # print(merge_sort(nn))
    # 奇偶排序
    print(odd_even_sort(nn))

    return


# 直接插入排序
def insert_sort(nn):
    # 从列表编号为1的位置 开始 循环
    for i in range(1, len(nn)):
        # j 存储 用于与 前j-1 个 比较大小的数字的下标
        j = i
        temp = nn[j]
        # 与 前 j-1 个 数字 比较大小
        while j > 0 and temp < nn[j-1]:
            nn[j] = nn[j - 1]
            j -= 1
        nn[j] = temp
    return nn


# 简单选择排序
def simple_select_sort(nn):
    for i in range(len(nn)):
        k = i
        for j in range(i + 1, len(nn)):
            if nn[j] < nn[k]:
                k = j
        temp = nn[i]
        nn[i] = nn[k]
        nn[k] = temp
    return nn


# 希尔排序
def shell_sort(nn):
    # 定义 增量
    d = int(len(nn)/2)
    # 判断 增量
    while d >= 1:
        # 从 d 位置开始 循环
        for i in range(d, len(nn)):
            temp = nn[i]
            j = i
            # 按照增量分组之后 进行 直接插入排序
            # 因为是按照增量分组 所以 j 每次 需要 大于 增量 d 的值
            while j >= d and temp < nn[j - d]:
                nn[j] = nn[j - d]
                j -= d
            nn[j] = temp
        # 增量每次减少到原来的一半
        d = int(d/2)
    return nn


# 快速排序
def quick_sort(nn):
    # 左标记
    left = 0
    # 右标记
    right = len(nn) - 1
    return quick_part_sort(left, right, nn)


# 快速排序
def quick_part_sort(i, j, nn):
    gg = i
    ll = j
    # 选取 左边第一个数为基数
    kk = nn[gg]
    if i < j:
        while i < j:

            # 判断小于基数的值
            while i < j and kk <= nn[j]:
                j -= 1
            nn[i] = nn[j]

            # 判断大于基数的值
            while i < j and nn[i] <= kk:
                i += 1
            nn[j] = nn[i]

        # 左标记 与 右标记重合时
        nn[j] = kk
        quick_part_sort(gg, j-1, nn)
        quick_part_sort(j + 1, ll, nn)
    return nn


# 归并排序
# TODO 另一种解法
def merge_sort(nn):
    # 左标记
    left = 0
    # 右标记
    right = len(nn)
    merge_sort_divide(left, right - 1, nn)
    return nn


# 分解
def merge_sort_divide(left, right, nn):
    # 左右 标记相等时 表明无法分割
    if left == right:
        return
    mid = int((left + right) / 2)
    # 分割左边
    merge_sort_divide(left, mid, nn)
    # 分割右边
    merge_sort_divide(mid + 1, right, nn)
    # 合并 左右 两部分
    merge_sort_merge(left, mid, right, nn)
    return


# 合并
def merge_sort_merge(left, mid, right, nn):
    # 定义一个临时列表
    temp = []
    # 定义两个 标记  分别在 左右 两部分的头部
    p, q = left, mid + 1
    # 比较两个子序列的数字的大小 把较小的 加入临时 列表中
    while p <= mid and q <= right:
        if nn[p] <= nn[q]:
            temp.append(nn[p])
            p += 1
        else:
            temp.append(nn[q])
            q += 1

    # 判断 哪个子序列中 还有数字 未加入到 临时列表中
    if p <= mid:
        for i in range(p, left+1):
            temp.append(nn[p])
            p += 1

    if q <= right:
        for i in range(q, right + 1):
            temp.append(nn[p])
            p += 1

    # 把临时列表中的元素复制到 原来的列表中
    for i in range(len(temp)):
        nn[i + left] = temp[i]
    return


# 奇偶排序
def odd_even_sort(nn):
    # 偶排序标志
    even_flag = False
    # 奇排序标志
    odd_flag = False
    # 当 奇排序 和 偶排序 都排序 完成后
    while (not even_flag) or (not odd_flag):
        even_flag = True
        odd_flag = True
        # 偶排序
        for i in range(len(nn) - 1):
            if nn[i] > nn[i + 1]:
                temp = nn[i]
                nn[i] = nn[i + 1]
                nn[i + 1] = temp
                i += 2
                even_flag = False

        # 奇排序
        for j in range(1, len(nn) - 1):
            if nn[j] > nn[j + 1]:
                temp = nn[j]
                nn[j] = nn[j + 1]
                nn[j + 1] = temp
                j += 2
                odd_flag = False

    return nn


# 堆排序
# TODO
def heap_sort(nn):

    return


# 臭皮匠排序
# TODO 最慢的排序
def sort(nn):
    return


# 冒泡排序
def bubble_sort(nn):
    for i in range(len(nn)):
        for j in range(len(nn) - 1):
            if nn[j] > nn[j + 1]:
                temp = nn[j]
                nn[j] = nn[j + 1]
                nn[j + 1] = temp
    return nn


# 8.写个函数，返回指定数在有序list中的位置，使用二分查找（折半查找实现）
def function8(nn, n):
    # 调用方法 生成n个数的list 并且 排序
    mm = bubble_sort(random_list(nn))
    # 左标记
    left = 0
    # 右标记
    right = len(mm) - 1
    # 调用二分查找
    kk = binary_search(left, right, n, mm)
    if kk == -1:
        print("所指定数字不存在list中")
    else:
        print("做指定数字在list中的位置为 %d" % kk)
    return


# 二分查找
def binary_search(left, right, n, mm):
    if left <= right:
        mid = int((left + right)/2)
        if mm[mid] == n:
            return mid
        elif mm[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
        return binary_search(left, right, n, mm)
    return -1


# 9.写个函数连接两个列表。
# 随机生成两个list A,B，写一个函数，连接A、B两个list
def function9(n, m):
    # 调用方法 生成n个数的list
    nn = random_list(n)
    mm = random_list(m)
    for i in range(len(mm)):
        nn.append(mm[i])
    return nn


# 10.写个函数交替合并两个列表，例如：[a,b,c], [1,2,3] → [a,1,b,2,c,3]。
# 写个函数交替合并题目9中的两个list，例如：A:[a,b,c], B:[1,2,3] → [a,1,b,2,c,3]。
def function10(n, m):
    # 调用方法 生成n个数的list
    nn = random_list(n)
    mm = random_list(m)
    # 定义一个 空的 list
    kk = []
    # 判断nn 和 mm 两个 list 的 大小
    if len(nn) < len(mm):
        kk = merge_list(kk, nn, mm)
    else:
        kk = merge_list(kk, mm, nn)
    return kk


# 交替 合并 两个 list
def merge_list(kk, nn, mm):
    # 遍历长度较小的 list
    for i in range(len(nn)):
        kk.append(nn[i])
        kk.append(mm[i])
    # 把 长度大的 list 剩下的 元素 依次加入到 新的 list 中
    for i in range(len(nn), len(mm)):
        kk.append(mm[i])
    return kk


# 11. 写个函数合并两个有序的列表。
def function11(n, m):
    # 调用方法 生成n个数的list 并且 排序
    nn = bubble_sort(random_list(n))
    mm = bubble_sort(random_list(m))
    # 定义一个 空的 list
    kk = []

    # 比较两个list的首位元素大小，把小的加到新的list中去 并且删除原来list中该元素
    # 循环操作 直至 某一个 list 长度为0  然后 把不为0的 那个list 剩下的元素加到 新的list 去
    while len(nn) > 0 and len(mm) > 0:
        if nn[0] > mm[0]:
            kk.append(mm[0])
            del mm[0]
        else:
            kk.append(nn[0])
            del nn[0]

    if len(nn) == 0:
        for i in range(len(mm)):
            kk.append(mm[i])
    else:
        for i in range(len(nn)):
            kk.append(nn[i])
    return


# 12.写个函数计算前100个Fibonacci数的列表。
def function12(n):
    for i in range(1, n+1):
        print(fib(i))
    return


def fib(i):
    # 用于存储 已经计算完的 数
    aa = [0 for i in range(1, 200)]
    if i == 1 or i == 2:
        return 1
    else:
        # 已经计算完的数 存储在数组中
        aa[i] = fib(i-1) + fib(i-2)
        return aa[i]


# 13.写个函数，返回指定数的各位数字的列表
def function13(n):
    # 定义一个 空的 list
    kk = []
    while int(n / 10) != 0:
        kk .append(n % 10)
        n = int(n / 10)
    kk.append(n)
    return kk


# 14.写个函数对两个数进行加减乘，使用各个位上的数字表示的列表实现并返回一个新的数字列表，
# 如果你有信心可以实现Karatsuba乘法。尝试不同的基数，如果你关心速度可以比较下哪个是最佳基数。
def function14(n, m):
    # 返回指定数字的列表
    kk = function13(n)
    ll = function13(m)

    # 获取 数字列表的长度
    a_length = len(kk)
    b_length = len(ll)
    # 乘法
    print(multiplication_num(n, a_length, m, b_length))

    # 加法
    print(add_num(kk, ll))
    # 减法
    print(subtract_num(kk, ll))

    return


# 数字列表 加法
def add_num(kk, ll):
    # 创建一个空列表
    gg = []
    # 给列表 填充0
    kk, ll = padding_zero(kk, ll)
    # 用于存储进位
    ff = 0

    for i in range(len(kk)):
        sum_num = kk[i] + ll[i] + ff
        if 9 < sum_num:
            ff = 1
        else:
            ff = 0
        gg.append(sum_num % 10)
    # 列表反转
    gg.reverse()
    return gg


# 数字列表 减法
def subtract_num(kk, ll):
    # 创建一个空列表
    gg = []
    # 给列表 填充0
    kk, ll = padding_zero(kk, ll)
    # 用于存储借位
    ff = 0

    for i in range(len(kk)):
        # 判断 减数 减去 借位 是否小于 被减数
        if kk[i] - ff < ll[i]:
            gg.append(10 + kk[i] - ll[i] - ff)
            ff = 1
        else:
            gg.append(kk[i] - ll[i] - ff)
            ff = 0
    # 列表反转
    gg.reverse()
    # 去掉 首位 0
    if gg[0] == 0:
        return gg[1:]
    return gg


# 数字列表 乘法
# Karatsuba (ac*10^2n + ((a+b)(c+d)-ac_bd)*10^n + bd)
# TODO 时间复杂度
def multiplication_num(aa, aa_length, bb, bb_length):
    # 如果 分解的 a 和 b 的大小为两位数 则可以 直接 相乘
    if aa < 10 or bb < 10:
        return aa * bb

    # 设定 基数值
    if aa_length < bb_length:
        n = int(bb_length/2)
    else:
        n = int(aa_length/2)

    # 设定分解的 a b
    if aa_length < n:
        a = 0
        a_length = 0
        b = aa
        b_length = aa_length
    else:
        a = int(aa / math.pow(10, n))
        a_length = aa_length - n
        b = int(aa % math.pow(10, n))
        b_length = get_number_length(b)

    # 设定分解的 c d
    if bb_length < n:
        c = 0
        c_length = 0
        d = bb
        d_length = bb_length
    else:
        c = int(bb / math.pow(10, n))
        c_length = bb_length - n
        d = int(bb % math.pow(10, n))
        d_length = get_number_length(d)

    # 计算 ac
    ac_multipl = multiplication_num(a, a_length, c, c_length)
    # 计算 bd
    bd_multipl = multiplication_num(b, b_length, d, d_length)
    # 计算 (a+b)(c+d)
    abcd_multipl = multiplication_num(a+b, get_number_length(a+b), d+c, get_number_length(d+c))

    # 计算结果 ac*10^2n + ((a+b)(c+d)-ac-bd)*10^n + bd
    result = int(ac_multipl * math.pow(10, n*2) + (abcd_multipl - ac_multipl - bd_multipl) * math.pow(10, n) + bd_multipl)

    return result


# 给列表 填充0
def padding_zero(kk, ll):
    # 判断 两个 list 长度的大小
    # 长度小的 补充0 至与另一个list长度相等
    if len(kk) < len(ll):
        for i in range(len(ll) - len(kk)):
            kk.append(0)
        return ll, kk
    else:
        for i in range(len(kk) - len(ll)):
            ll.append(0)
        return kk, ll


# 获取 数字的长度
def get_number_length(n):
    if n == 0:
        return 1
    else:
        m = n
        i = 0
        while m > 0:
            m = int(m / 10)
            i += 1
    return i


# 15.写个函数测试一个字符串是否是回文。
def function15(mm):
    # 左标记
    left = 0
    # 右标记
    right = -1
    # 是否回文的标志
    flag = False
    # 循环字符串一半的长度
    while left < int(len(mm)/2):
        if mm[left] == mm[right]:
            left += 1
            right += -1
            flag = True
        else:
            flag = False
            break
    if flag is False:
        print("该字符串不是回文")
    else:
        print("该字符串是回文")
    return


# 16.写一个函数将一段文本text大小写互换
def function16():
    # 读取一个文件
    with open('./data/test', 'r+', encoding='utf8') as f:
        # 读取文件中的多行内容
        data = f.readlines()
        # 移动文件读取指针到 文件开始位置
        f.seek(0)
        # 清空文件
        f.truncate()
        for i in range(len(data)):
            f.write(data[i].lower())
    return


# 17.写个函数，给定一个字符串列表并按下面表示打印出来，一行一个打印在矩形框中
'''
# 例如列表["Hello", "World", "in", "a", "frame"] 打印的结果是：
# *********
# * Hello *
# * World *
# * in    *
# * a     *
# * frame *
# *********
'''


def function17(kk):
    # 存储 列表中最大的字符串的长度
    mm = 0
    for i in range(len(kk)):
        # 获取字符串的长度
        nn = len(kk[i])
        if mm < nn:
            mm = nn
    # 打印 上边框
    print("*"*(mm+4))
    j = 0
    # 循环 列表
    while j < len(kk):
        print("* %s" % kk[j], end="")
        print(" "*(mm-len(kk[j])+1) + "*")
        j += 1
    # 打印 下边框
    print("*"*(mm + 4))
    return


# 18.写函数将一段文本text翻译为Pig Latin返回。
'''
英语翻译为Pig Latin的规则是：取出每个单词的首个字母，追加’ay’后再放到该单词的末尾
例如“The quick brown fox” 翻译后就变成了 “Hetay uickqay rownbay oxfay”。
'''
def function18():
    # 读取一个文件
    with open('./data/test', 'r+', encoding='utf8') as f:
        # 读取文件中的多行内容
        data = f.readlines()
        # 移动文件读取指针到 文件开始位置
        f.seek(0)
        # 清空文件
        f.truncate()
        # 用于存储 翻译后的 的内容
        content = ""

        for i in range(len(data)):
            kk = data[i]
            # 以空格分割
            gg = kk.split(" ")
            for j in range(len(gg)):
                ll = gg[j]
                content += (ll[1:len(ll)] + ll[0] + "ay") + " "
        f.write(content.capitalize())
    return


if __name__ == '__main__':
    function7(10)

