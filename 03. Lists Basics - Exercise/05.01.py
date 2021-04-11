cards = input().split()
n = int(input())

half = int(len(cards) // 2)
result = []

for number_of_shuffle in range(n):
    result = []
    for index in range(len(cards)):
        if index == len(cards) / 2:
            break
        one = cards[index]
        right_side = index + half
        two = cards[right_side]
        result.append(one)
        result.append(two)
    cards = result
print(result)