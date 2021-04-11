patern = int(input())

for row in range(1, patern+1):
    print("*"*row)

for neg_row in range(patern-1, 0, -1):
    print('*'*neg_row)