line1 = input().split(" ")
line2 = input().split(" ")
line3 = input().split(" ")
all_lines = [line1, line2, line3]
player1 = []
player2 = []

for line in all_lines:
    for index, player in enumerate(line):
        if player == '1':
            player1.append(index)
        elif player == '2':
            player2.append(index)

players = [player1, player2]
winning_patterns = [[0, 1, 2], [0, 0, 0], [1, 1, 1], [2, 2, 2], [2, 1, 0]]

for index, player in enumerate(players):
    if index == 0 and player in winning_patterns:
        print("First player won")
        break
    if index == 1 and player in winning_patterns:
        print("Second player won")
        break
    elif index == 1 and not (player in winning_patterns):
        print("Draw!")