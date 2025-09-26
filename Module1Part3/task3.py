meters = float(input())
print("Выберете еденицу для перевода")
print("1 - Мили ")
print("2 - Дюймы ")
print("3 - Ядры ")
choice = input(" Введите номер операции (1, 2, или 3):")
if choice == "1":
    miles = meters * 0.621371
    print(f"{meters} = {miles}")
elif choice == "2":
    inches = meters * 39.3701
    print(f"{meters} = {inches}")
elif choice == "3":
    yards = meters * 1.0936
    print(f"{meters} = {yards}")