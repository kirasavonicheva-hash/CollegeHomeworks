print("Введите два числа (начало и конец диапазона):")
a = int(input("начало диапазона:"))
b = int(input("конец диапазона:"))
print()
if a == b:
    raise RuntimeError("Числа не могут быть одинаковыми")
for i in range(a, b):
    if i % 3 == 0:
        i = "Fizz"
        print(i, end="")
print()
for i in range(a, b):
    if i % 5 == 0:
        i = "Buzz"
        print(i, end="")
print()
for i in range(a, b):
    if i % 3 == 0 and i % 5 == 0:
        i = "Fizz Buzz"
        print(i, end="")
print()
for i in range(a, b):
    if i % 3 != 0 and i % 5 != 0:
        print(i, end="")
print()