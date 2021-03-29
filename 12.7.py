per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('введите сумму вклада: '))
per = list(per_cent.values())
deposit = []
for i in per:
    i = i * money / 100400
    print(i)
    deposit.append(i)
print('deposit= ', deposit)
deposit_m = max(deposit)
print('Максимальная сумма, которую вы можете заработать —', deposit_m)


