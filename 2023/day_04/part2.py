import sys

input = sys.stdin.read().strip()

og_scratchcards = []
idx = 0
for line in input.split("\n"):
    _, nums = line.split(":")

    og_scratchcards.append(nums)
    idx += 1

num_scratchcards = [1 for _ in range(len(og_scratchcards))]

for idx, num_scratchcard in enumerate(num_scratchcards):
    nums = og_scratchcards[idx]

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

    for i in range(idx + 1, idx + num_wins + 1):
        if i > len(og_scratchcards):
            break
        
        num_scratchcards[i] += num_scratchcard

print(sum(num_scratchcards))
