# 冒泡排序
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    a = [5, 3, 7, 9, 22, 66, 99, 87, 32, 45, 345, 525]
    bubbleSort(a)
    print(a)
