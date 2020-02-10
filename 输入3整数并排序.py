# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#
# 程序分析：我们想办法把最小的数放到x上，
# 先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

l = []
for i in range(0,3):
    x = input("输入数字")
    l.append(x)
l.sort()

print(l)

# 题目：斐波那契数列。
# # 程序分析：斐波那契数列（Fibonacci sequence），
# # 又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……。
# # 在数学上，费波那契数列是以递归的方法来定义：


def fib(n):
    sum = 1
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a + b
        sum += a
    return sum

print(fib(1))
