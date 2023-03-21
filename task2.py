import math

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

d = s*s - 4*p
if d < 0:
    print('Неверные данные')
    exit(1)
else:
    y = (s + math.sqrt(d)) / 2

x = p / y
print(f'Числа: "{x} и {y}"')