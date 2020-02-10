# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

a = ['x', 'y', 'z']

#
# for i in jia:
#     for j in yi:
#         if i == 'x'and j != 'a':
#             print(i, j)
#             if j == 'c' and i != 'y':
#                 print(i, j)
for i in a:
    for j in a:
        if i != j:
            for k in a:
                if (i != k) and (j != k):
                    if (i != 'x') and (k != 'x') and (k != 'z'):
                        print('order is a -- %s\t b -- %s\tc--%s' % (i, j, k))