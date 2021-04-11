population = [int(n) for n in input().split(", ")]
wealth = int(input())
wealthiest = max(population)
difference = 0
index_of_the_last_item = len(population) -1

for n in range(len(population)):
    if population[n] < wealth:
        wealthiest = max(population)
        difference = wealth - population[n]
        if wealthiest - difference >= wealth:
            population[population.index(wealthiest)] -= difference
            population[n] += difference

if sum(population) >= len(population) * wealth:
    print(f'{population}')
else:
    print('No equal distribution possible')