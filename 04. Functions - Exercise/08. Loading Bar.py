def load_bar(n):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."] # or ["." * 10]
    if n == 0:
        return bar
    n = n // 10
    for i in range(n):
        bar[i] = '%'
    return bar


number = int(input())
bar_result = load_bar(number)

if bar_result.count('%') == 10:
    print('100% Complete!')
    print(f'[{"".join(bar_result)}]')
else:
    print(f"{number}% [{''.join(bar_result)}]")
    print('Still loading...')