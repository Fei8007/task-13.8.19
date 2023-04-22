tickets = int(input('Введите количество билетов: '))

amount = 0

for i in range(tickets):
    age = int(input('Введите возраст: '))
    print('age', age)
    if age < 18:
        amount += 0
        print('from < 18 - 0 рублей')
    elif 18 <= age < 25:
        amount += 990
        print('from 18 to 25 - 990 рублей')
    else:
        amount += 1390
        print('from 25+ - 1390 рублей')

if tickets >= 3:
    discount = (amount / 100) * 10
    amount = amount - discount

print('Общая сумма c учетом скидки: ', int(amount))
