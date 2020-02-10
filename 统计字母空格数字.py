# 计算任意字符串中字母，空格，数字出现的次数

str = input("输入任意字符串:")

num = 0
letter = 0
space = 0

for i in str:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        num += 1
    elif i.isspace():
        space += 1

print("字母：%d，数字：%d，空格：%d" % (letter, num, space))

