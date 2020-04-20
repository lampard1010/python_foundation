n = input("please input a num:")
print(n)
num = int(n)
num1 = int(num / 1000)
num2 = int(num % 1000 / 100)
num3 = int(num % 100 / 10)
num4 = int(num % 10)

print(num1, num2, num3, num4)

a = [num1, num2, num3, num4]
b = []
for i in a:
    b.append((i + 5) % 10)
print(b)
b.reverse()
print(b)