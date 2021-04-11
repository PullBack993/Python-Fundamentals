budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = (price_flour*0.25)+price_flour
for_one_milk = price_milk / 4

total = price_eggs + for_one_milk + price_flour

counter_eggs = 0
cozonac = 0
day = 0
left_money = 0
while budget > total:
    budget -= total
    cozonac += 1
    counter_eggs += 3
    day += 1
    if day == 3:
        day = 0
        counter_eggs -= cozonac - 2
print(f"You made {cozonac} cozonacs! Now you have {counter_eggs} eggs and {budget:.2f}BGN left.")
    


