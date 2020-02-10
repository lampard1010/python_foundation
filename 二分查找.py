# 二分查找(已排序数组)

def binary_search(num_list, item):
    low = 0
    high = len(num_list)
    while low <= high:
        mid = int((low + high) / 2)
        guess = num_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    num_list = [3, 4, 66, 77, 456, 3224]
    item = 3224
    print(binary_search(num_list, item))
