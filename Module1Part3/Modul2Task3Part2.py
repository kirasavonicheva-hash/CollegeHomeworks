print("Введите число")
number = int(input())
for i in range(8):
   print("{0}^{1} = {2}".format(number, i, number**i))