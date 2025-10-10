tariffs = \
    {
        "MTS": 5.0,
        "Билайн": 1.2,
        "Megafon": 1.8,
        "Tele2": 1.0
    }
print("Tele2")
print("MTS")
a = input("Введите номер вашего оператора:")
b = input("Введите номер оператора, которому вы звоните:")
if a == "MTS" and b == "MTS":
    print(100*3)
if a == "MTS" and b == "Megafon":
    print(100*2)
if a == "MTS" and b == "Tele2":
    print(100*1)
if a == "Tele2" and  b == "Tele2":
    print(100*1)
if a == "Tele2" and b == "Megafon":
    print(100*2)
if a == "Megafon" and b == ("Megafon"):
    print(100*1)