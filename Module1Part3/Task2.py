number = int(input())
number = list(str(number))
sum = 1
for i in number:
    sum *= int(i)
print(sum)