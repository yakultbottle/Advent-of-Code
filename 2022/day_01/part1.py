input = open(0).read().strip()

most_calories = -1
for elf in input.split("\n\n"):
    calories = 0
    for food in elf.split("\n"):
        calories += int(food)
    most_calories = max(calories, most_calories)

print(most_calories)
