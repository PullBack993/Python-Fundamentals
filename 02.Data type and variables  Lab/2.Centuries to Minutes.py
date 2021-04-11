centuries = int(input())

years = centuries * 100
day = int(years * 365.24220)
hours = day * 24
minutes = hours * 60

print(f'{centuries} centuries = {years} years = {day} days = {hours} hours = {minutes} minutes')