deck = input().split()
number_of_shuffles = int(input())

left_half = []
right_half = []

for shuffels in range(number_of_shuffles):
    current_deck = []
    half = int(len(deck)/2)
    left_half = deck[0:half]
    right_half = deck[half::]

    for index_of_cars in range(len(left_half)):
        current_deck.append(left_half[index_of_cars])
        current_deck.append(right_half[index_of_cars])
    deck = current_deck

print(deck)