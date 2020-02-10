# 石头1剪刀2布3
import random

player = int(input("请出拳："))
computer = int(random.randint(1,3))
print("玩家出拳：%d - 电脑出拳：%d" % (player,computer))

if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("win")
elif player == computer:
    print("平手")
else:
    print("lose")

