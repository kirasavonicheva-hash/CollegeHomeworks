def f(numm):
    for x in range(2, numm + 1):
        if x != numm:
            if numm % x == 0:
                break
        else:
            print(numm)

while True:
    try:
        n1 = int(input())
        n2 = int(input())
        for x in range(n1, n2):
            f(x)
    except ValueError:
        print("Не правильные входные данные")
