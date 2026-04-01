input = open(0).read().strip()

most_calories = -1
second_most = -1
third_most = -1
for elf in input.split("\n\n"):
    calories = 0
    for food in elf.split("\n"):
        calories += int(food)

    if calories > most_calories:
        third_most = second_most
        second_most = most_calories
        most_calories = calories
    elif calories > second_most:
        third_most = second_most
        second_most = calories
    elif calories > third_most:
        third_most = calories

ans = most_calories + second_most + third_most
print(ans)
