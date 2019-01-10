month_num = int(input())

if month_num == 2:
    print(28)
elif not 0 < month_num < 13:
    print(0)
elif month_num > 7:
    print(30 + (month_num + 1) % 2)
else:
    print(30 + month_num % 2)
