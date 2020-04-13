str = input("input something:\n")

str = str.upper()

print(str)

f1 = open("test.txt", "w")
f1.write(str)

f2 = open("test.txt", "r")
print(f2.read())

f1.close()
f2.close()