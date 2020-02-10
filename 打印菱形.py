for i in range(-4, 5):
    if i < 0:
        j = -i
    elif i >= 0:
        j = i
    print(" " * j, "*" * (9 - 2 * j), " " * j)
