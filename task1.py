from random import randint

coins_count = int(input("Введите количество монет: "))
coins = []

for i in range(coins_count):
    coins.append(randint(0, 1))

print(coins)

tails_count = 0
heads_count = 0

for coin in coins:
    if coin == 0:
        heads_count += 1
    else:
        tails_count += 1

min_coins = heads_count if heads_count < tails_count else tails_count

print(f'Минимальное количество монет: "{min_coins}"')