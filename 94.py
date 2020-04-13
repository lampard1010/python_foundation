import time
import random

start = time.time()
print("start:%0.2fs" % start)
while True:
    play = input('play the game(y/n)?')
    if play == 'y':
        number = random.randint(0, 1000)
        guess = int(input('guess a number: '))
        while True:
            if number > guess:
                guess = int(input("guess a bigger number: "))
            elif number < guess:
                guess = int(input("guess a smaller number: "))
            else:
                end = time.time()
                print("end:%0.2fs" % end)
                print("bingo! ")
                print(u"%0.2fs耗时：" % (end - start))
                break
    else:
        break
