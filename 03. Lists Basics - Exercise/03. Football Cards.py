cards = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


for card in cards:
    team, player = card.split('-')
    player = int(player)

    if team == 'A':
        if player in team_a:
            team_a.remove(player)
        if len(team_a) < 7:
            print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
            print('Game was terminated')
            quit()

    elif team == 'B':
        if player in team_b:
            team_b.remove(player)
        if len(team_b) < 7:
            print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
            print('Game was terminated')
            quit()

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')