# 文件组合

import string

f1 = open("1.txt", encoding="utf-8")
a = f1.read()

f2 = open("2.txt", encoding="utf-8")
b = f2.read()

l = list(a+b)
l.sort()
s = ""
s = s.join(l)

print(s)