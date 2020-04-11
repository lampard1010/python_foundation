x = int(input("请打印一个不超过5位的数字："))

a = int(x / 10000)
b = int(x % 10000 / 1000)
c = int(x % 1000 / 100)
d = int(x % 100 / 10)
e = int(x % 10)

print(a, b, c, d, e)
