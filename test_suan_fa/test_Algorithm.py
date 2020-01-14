# 二分查找
def binary_search(list, n):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right)//2
        if list[mid] == n:
            print("列表中存在该元素")
            return
        if list[mid] < n:
            left = mid + 1
        if list[mid] > n:
            right = mid - 1
    print("列表中不存在该元素")


# 选择排序
def select_sort(list):
    for i in range(len(list)):
        m = i
        for j in range(i+1, len(list)):
            if list[j] < list[m]:
                m = j
        temp = list[m]
        list[m] = list[i]
        list[i] = temp
    print(list)


#


if __name__ == '__main__':

    # binary_search([1, 2, 3, 5, 6, 10], 9)
    select_sort([7, 2, 3, 6, 6, 10])



