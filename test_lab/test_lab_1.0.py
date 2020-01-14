import random
import datetime
import math
#  初级 1.0


# 1.写程序将” Hello World”打印到屏幕
def function1():
    print("Hello World")
    return


# 2.写程序输入用户的姓名并用该姓名和他打招呼。
def function2(name):
    if name == "":
        print("请输入姓名")
    print(name + "你好")
    return


# 3.修改上一个程序，使得仅可以与Alice和Bob这两个用户用其姓名与之打招呼
def function3(name):
    if name == "":
        print("请输入姓名")
    if name != "Alice" and name != "Bob":
        print("您输入的姓名有误，请重新输入")
    else:
        print(name + "你好")
    return


# 4.写程序输入一个数n并打印出从1到n的和。
def function4(n):
    # 计算 1 到 n 的和
    m = ((1+n)*n)/2
    print(m)
    return


# 5.修改上个程序，使得求和的数只包含3或5的倍数，例如n=17，则求和的数为：3, 5, 6, 9, 10, 12, 15。
def function5(n):
    # 存储 数的和
    m = 0
    if n < 3:
        print("请输入大于等于3的数字")
    else:
        # 从3开始循环
        for i in range(3, n+1):
            # 判断是否为 3或5的倍数
            if i % 3 == 0 or i % 5 == 0:
                m += i
    print(m)
    return


# 6.写个程序，要求用户输入一个数n，并随机性地选择是计算1到n的和还是计算1到n的乘积。
def function6(n):
    m = random.randint(1, 10)
    if m % 2 == 0:
        function4(n)
    else:
        function_multiply(n)
    return


# 1 到 n 的乘积
def function_multiply(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    print(m)
    return


# 7.写程序打印出12×12乘法表（对齐，格式化输出）。
def function7(n):
    for i in range(1, n+1):
        for m in range(1, i+1):
            # end='\t' 为了对齐 每一列
            print("%d*%d=%d" % (m, i, i*m), end='\t')
        print("")
    return


# 8.写程序打印所有的素数（系统最大整数范围内的）。
def function8(n):
    if n < 1:
        print("请输入大于1的数字")
    # 从2开始循环
    for i in range(2, n+1):
        # 是否为素数的标记
        k = True
        # 除去 要判断的 数字中 本身 循环 从2 到 该数字 前一位的数字 判断是是否 被整除
        for m in range(2, int(i/2)+1):
            if i % m == 0:
                k = False
                break
        if k is True:
            print(i)
    return


# 9.写一个竞猜游戏，用户必须猜一个秘密的数字，在每次猜完后程序会告诉用户他猜的数是太大了还是太小了，直到猜测正确
# 最后打印出猜测的次数。如果用户连续猜测同一个数字则只算一次（注意用户交互方法）。
def function9():
    # 随机生成一个数字 当做 要猜测的数字
    m = random.randint(1, 100)
    print("请输入你认为的数字")
    k = 0
    while True:
        n = input()
        k += 1
        if int(n) < m:
            print("你猜测的数字小了")
        elif int(n) > m:
            print("你猜测的数字大了")
        else:
            print("你猜对了数字了")
            print(k)
            break
    return


# 10.写个程序打印出接下来的20个闰年（输出格式美观）
def function10():
    # 获取当前 年份
    nn = datetime.datetime.now().year
    # 计数
    m = 0
    while True:
        # 能被4整除 且不能被100整除 为闰年
        if nn % 4 == 0 and nn % 100 != 0:
            print(nn)
            m += 1
        nn += 1
        if m == 20:
            break
    return


# 11.
def function11():
    # n 为 分数的正负号
    n = 2
    # m 为分母
    m = 1
    zz = 0.0
    for i in range(1, int(math.pow(10, 6))+1):
        zz += math.pow(-1, n)*(1/m)
        n += 1
        m += 2
    print(4*zz)
    return

