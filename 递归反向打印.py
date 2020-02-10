# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


if __name__ == '__main__':
    str = input("用户输入字符串：")
    output(str, len(str))

# 非递归
# str = "abcdefg"
#
# for i in range(len(str)):
#     print(str[-i - 1])