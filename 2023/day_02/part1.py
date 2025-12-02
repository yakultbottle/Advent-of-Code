import sys

input = sys.stdin.read()

def is_valid(sets: str) -> bool:
    for temp in sets.split("; "):
        for ball in temp.split(", "):
            num, colour = ball.split(" ")

            if colour == "red":
                if int(num) > 12:
                    return False
            elif colour == "green":
                if int(num) > 13:
                    return False
            elif colour == "blue":
                if int(num) > 14:
                    return False
            else:
                print("What on earth")
                return False
    return True

answer = 0
for line in input.strip().split("\n"):
    game, sets = line.split(": ")

    if is_valid(sets):
        answer += int(game.split(" ")[-1])

print(answer)
