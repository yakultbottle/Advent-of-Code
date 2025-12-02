input = open(0).read().strip()

rotations = [(line[0], int(line[1:])) for line in input.split("\n")]

dial_position = 50
ans = 0
for direction, amount in rotations:
    if direction == "L":
        dial_position -= amount
    else:
        dial_position += amount

    dial_position %= 100

    if dial_position == 0:
        ans += 1

print(ans)
