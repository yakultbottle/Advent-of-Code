import sys

input = sys.stdin.read()

def power(sets: str) -> int:
    min_red = 0
    min_blue = 0
    min_green = 0

    for temp in sets.split("; "):
        for ball in temp.split(", "):
            num, colour = ball.split(" ")

            if colour == "red":
                min_red = max(min_red, int(num))
            elif colour == "green":
                min_green = max(min_green, int(num))
            elif colour == "blue":
                min_blue = max(min_blue, int(num))
            else:
                print("What on earth")
                return 0

    return min_red * min_green * min_blue

answer = 0
for line in input.strip().split("\n"):
    game, sets = line.split(": ")

    answer += power(sets)

print(answer)
