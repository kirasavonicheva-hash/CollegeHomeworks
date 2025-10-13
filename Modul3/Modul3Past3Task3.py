print("Введите два числа (начало и конец диапазона):")
a = int(input("начало диапазона:"))
b = int(input("конец диапазона:"))
print()
if a == b:
    raise ("Числа не могут быть одинаковыми")
for i in range(a, b):
    if i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    elif i % 15 == 0:
        i = "Fizz Buzz"
    print(i,end="\n\n")