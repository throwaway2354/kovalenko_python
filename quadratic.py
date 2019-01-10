from decimal import Decimal


a = Decimal(input('a = '))
b = Decimal(input('b = '))
c = Decimal(input('c = '))

if a == 0:
    if b == 0:
        if c == 0:
            print('любое число')
        else:
            print('корней нет')
    else:
        x = -c / b

        assert b * x + c == 0

        print(x)
else:
    d = b ** 2 - 4 * a * c

    if d >= 0:
        x1 = (-b + d.sqrt()) / (2 * a)
        x2 = (-b - d.sqrt()) / (2 * a)

        assert a * (x1 ** 2) + b * x1 + c == 0
        assert a * (x2 ** 2) + b * x2 + c == 0

        if x1 == x2:
            print(x1)
        else:
            print(x1, x2)
    else:
        print('действительных корней нет')
