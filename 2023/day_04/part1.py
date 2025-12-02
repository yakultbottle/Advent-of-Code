import sys

input = sys.stdin.read().strip()

answer = 0
for line in input.split("\n"):
    _, nums = line.split(":")

    num_wins = 0
    winnings, numbers = nums.split("|")

    wins = set()
    for num in winnings.strip().split():
        wins.add(num)

    printer = []
    for num in numbers.strip().split():
        if num in wins:
            printer.append(num)
            num_wins += 1

    answer += int(2 ** (num_wins - 1))

print(answer)
