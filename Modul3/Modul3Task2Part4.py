n, m, a = int(input()), 1, 0
while n != 0:
    d, n = n % 10, n // 10
    if d not in { 3, 6 }:
        a, m = a + d * m, m * 10
print(a)