a = 0
b_max = 0
c_min = 0
while (True):
    a = int(input("Введите число:"))
    c_min += a
    if a == 7:
        print("Пока:")
        break
    elif a > b_max:
        b_max = a
print("Сумма введенных чисел равна", c_min)
print("Максиммальное из введенных чисел это - ", b_max)