input = open(0).read().strip()

rotations = [(line[0], int(line[1:])) for line in input.split("\n")]

dial_position = 50
ans = 0
for direction, amount in rotations:
    og_position = dial_position

    if direction == "L":
        dial_position -= amount
    else:
        dial_position += amount

    if og_position != 0 and dial_position < 0:
        ans += 1
    elif dial_position == 0:
        ans += 1

    ans += abs(dial_position) // 100
    dial_position %= 100


print(ans)
