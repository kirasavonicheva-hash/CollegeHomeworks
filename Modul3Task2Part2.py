try:
    length_str = input("Введите длину линии: ")
    length = int(length_str)

    symbol = input("Введите символ для заполнения: ")

    if not symbol:
        print("Ошибка: Символ не может быть пустым.")
    else:
        for _ in range(length):
            print(symbol)

except ValueError:
    print("Ошибка: Введена некорректная длина. Пожалуйста, введите число.")