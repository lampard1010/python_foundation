# 输入字符直到#为止

f = open("97.txt", 'w')

for i in range(10):
    str = input("请输入字符：\n")
    if str == "#":
        break
    else:
        f.write(str)
