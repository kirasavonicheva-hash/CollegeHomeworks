a = int(input())
b = int(input())
sum = 0
count = 0
sumch = 0
count1 = 0
sumch9 = 0
count2 = 0

for i in range(a, b+1):
    if i % 2 == 0:
        sum += i
        count += 1
    if i % 2 != 0:
        sumch += i
        count1 += 1
    if i % 9 == 0:
        sumch9 += i
        count2 += 1
print("СРЕДНЕАРИФМ не четных", sumch/count1)
print("Средние арифметическое четных", sum/count)
print("Средниеарифметическое кратных на 9", sumch9/count2)
