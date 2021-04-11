n = int(input())
positives = []
negatives = []

for i in range(n):
    n_lines = int(input())
    if n_lines > 0:
        positives.append(n_lines)
    else:
        negatives.append(n_lines)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')