import sys

input = sys.stdin.read()

nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
answer = 0
for line in input.strip().split("\n"):
    left = 0
    right = len(line) - 1

    while line[left] not in nums:
        left += 1
    while line[right] not in nums:
        right -= 1

    answer += int(line[left]) * 10 + int(line[right])

print(answer)
