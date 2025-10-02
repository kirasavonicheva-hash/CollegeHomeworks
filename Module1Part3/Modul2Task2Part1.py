days = {
    1 : "понедельник",
    2 : "вторник",
    3 : "среда",
    4 : "четверг",
    5 : "пятница",
    6 : "суббота",
    7 : "воскресенье"
    }

day_numbers = int(input())
if 1 <= day_numbers <= 7:
    print(days[day_numbers])
