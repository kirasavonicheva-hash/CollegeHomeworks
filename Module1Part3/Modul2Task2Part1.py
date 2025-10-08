a = int(input())
b = int(input())

odd = 0
oddCount = 0
even = 0
evenCount = 0
multiples = 0
multiplesCount = 0
arithmetic_mean = 0
arithmetic_meanCount = 0

for i in range(a,b+1):
    if i % 2!= 0:
        odd += i
        oddCount += 1
    if i%2==0:
        even+=i
        evenCount += 1
    if i%9==0:
        multiples+=i
        multiplesCount += 1
    if  i%10==0:
        arithmetic_mean+=i
        arithmetic_meanCount += 1

print("Сумма нечетных: ",odd / oddCount)
print("Сумма четных: ",even / evenCount)
print("Сумма кратных на 9: ",multiples / multiplesCount)
print("Сумма среднеарифметических",arithmetic_mean / arithmetic_meanCount)