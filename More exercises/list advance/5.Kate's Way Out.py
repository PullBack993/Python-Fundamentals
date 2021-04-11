rows = int(input())
way_out = True
stop_row_index = []
move_counter = 0
counter = 0
way_index = []
start_row_index = [] # we started from there !
start = []
for row in range(rows):
    maze = input()
    for a, i in enumerate(maze):
        if 'k' == i:
            start_row_index = [int(row)]
            start = [i]
            way_out = True
            move_counter += 1
        elif i == '#':
            counter += 1
            if counter == len(maze):
                stop_row_index = [int(row)]
        elif i == ' ':
            way_index.append(a)
            move_counter += 1
    if counter == len(maze):#and len(maze) == maze[rows::-1]:
        way_out = False
    counter = 0

step_counter = 0
difference = rows - start_row_index[0]
for d in range(1, difference+1):
    for way in way_index:
        if d == way:
            step_counter += 1
        if difference == step_counter:
            way_out = True

if way_out:
    print(f'Kate got out in {move_counter} moves')
else:
    print('Kate cannot get out')