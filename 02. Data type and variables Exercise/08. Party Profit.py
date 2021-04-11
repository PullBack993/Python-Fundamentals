import math
party_size = int(input())
days = int(input())

coin_counters = 0

for day in range(1, days+1):
    if day % 10 == 0:
        party_size -= 2

    if day % 15 == 0:
        party_size += 5

    coin_counters += (50 - 2 * party_size)

    if day % 3 == 0:
        coin_counters -= party_size * 3

    if day % 5 == 0:
        coin_counters += 20 * party_size
        if day % 3 == 0:
            coin_counters -= 2 * party_size

print(f'{party_size} companions received {math.floor(coin_counters / party_size)} coins each.')