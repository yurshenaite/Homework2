s, r = float(input()), float(input())
cost = s + r
price = (cost * 100) % 100
print(f'Сумма двух шоколадок составила {int(cost)} рублей {int(price)} копеек')