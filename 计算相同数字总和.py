sum = 0

t = int(input("a的数量："))
a = int(input("a的值："))
x = a

for i in range(0, t):
    sum += x
    x = x * 10 + a
print(sum)
