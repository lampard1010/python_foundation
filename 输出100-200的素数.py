# 输出100-200的素数
# 什么是素数：只有能被1和自身整除的是素数

li = []
for i in range(100, 201):
    for j in range(2, i):
        if i % j == 0:
            if i in li:
                li.remove(i)
            break
        if i % j != 0:
            if i in li:
                continue
            else:
                li.append(i)
            continue
print(li)

for i in range(100, 201):
    leap = 1
    for j in range(2, i):
        if i % j == 0:
            leap = 0
            break
    if leap == 1:
        print(i)
