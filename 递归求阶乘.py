# 题目：利用递归方法求5!。
#
# 程序分析：递归公式：fn=fn_1*4!

def fon(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fon(j - 1)
    return sum

if __name__ == '__main__':
    print(fon(6))