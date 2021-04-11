cards = input().split(":")
deck = []
command = input()

while not command == 'Ready':
    data = command.split()
    name = data[0]
    if name == 'Add':
        if data[1] in cards:
            save_the_card = data[1]
            cards.remove(data[1])
            deck.append(save_the_card)
        else:
            print('Card not found.')
    elif name == 'Insert':
        index = data[2]
        index = int(index)
        if data[1] in cards and 0 <= index <= len(cards):
            card_save = data[1]
            cards.remove(data[1])
            index = data[2]
            index = int(index)
            deck.insert(index, card_save)
        else:
            print('Error!')
    elif name == 'Remove':
        if data[1] in deck:
            deck.remove(data[1])
        else:
            print('Card not found.')
    elif name == 'Swap':
        fist = deck.index(data[1])
        second = deck.index(data[2])
        deck.remove(data[1])
        deck.remove(data[2])
        deck.insert(fist, data[2])
        deck.insert(second, data[1])
    elif name == 'Remove':
        deck.remove(data[1])
    elif name == 'Shuffle':
        deck.reverse()

    command = input()

print(" ".join(deck))