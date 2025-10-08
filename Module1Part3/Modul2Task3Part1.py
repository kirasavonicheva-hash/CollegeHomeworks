number = int(input("Введите число от 1 до 100: "))

if number < 1 or number > 100:
    print("Ошибка: число должно быть в диапазоне от 1 до 100")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)