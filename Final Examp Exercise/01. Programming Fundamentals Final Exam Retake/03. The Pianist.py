from collections import defaultdict
number = int(input())
pieces = defaultdict(dict)
for n in range(number):
    piece, composer, key = input().split("|")
    pieces[piece]['key'] = key
    pieces[piece]['composer'] = composer

command = input()

while not command == 'Stop':
    command_name = command.split("|")
    if command_name[0] == 'Add':
        piece = command_name[1]
        composer = command_name[2]
        key = command_name[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            print(f"{piece} by {composer} in {key} added to the collection!")
            pieces[piece]['key'] = key
            pieces[piece]['composer'] = composer
    elif command_name[0] == 'Remove':
        piece = command_name[1]
        if piece in pieces:
            print(f"Successfully removed {piece}!")
            del pieces[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command_name[0] == 'ChangeKey':
        piece = command_name[1]
        new_key = command_name[2]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_pieces = sorted(pieces.items(), key=lambda tkvp: (tkvp[0], tkvp[1]['composer']))
for piece, value in sorted_pieces:
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")