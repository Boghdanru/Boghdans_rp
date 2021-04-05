s = True
while s:
    try:
      count = int(input('введите количество билетов:'))
    except ValueError as e:
        print('ввели неправильно')
    else:
      ticket_cost = []
      s = False
for i in range(count):
    if i == 0:
        s = True
        while s:
            try:
              age = int(input('введите возраст первого посетителя '))
            except ValueError as e:
                print('ввели неправильно')
            else:
                s = False
    else:
        s = True
        while s:
            try:
              age = int(input('введите возраст следующего посетителя '))
            except ValueError as e:
                print('ввели неправильно')
            else:
                s = False

    if 18 < age < 25:
        ticket_cost.append(990)
    elif age >= 25:
        ticket_cost.append(1390)
cost = sum(ticket_cost)
if count > 3:
    cost = int(0.9 * cost)
print('сумма к оплате: ', cost)
