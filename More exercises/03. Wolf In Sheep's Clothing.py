array = input().split(", ")

if array.pop() == "wolf":
    print("Please go away and stop eating my sheep")
    raise SystemExit

arr_reversed = array[::-1]

for i in range(len(arr_reversed)):
    if arr_reversed[i] != "sheep":
        print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")