import sys

towels, patterns  = [thing.strip() for thing in sys.stdin.read().split("\n\n")]

patterns = [pattern.strip() for pattern in patterns.split("\n")]
towels = [towel.strip() for towel in towels.split(", ")]

memo = {}
def is_valid(pattern: str, idx: int) -> bool:
    if pattern[idx:] in memo:
        return memo[pattern[idx:]]

    if idx >= len(pattern):
        return False

    if pattern[idx:] in towels:
        memo[pattern[idx:]] = True
        return True
    
    for towel in towels:
        if pattern[idx:(idx + len(towel))] == towel and is_valid(pattern, idx + len(towel)):
            memo[pattern[idx:]] = True
            return True

    memo[pattern[idx:]] = False
    return False

count = 0
for pattern in patterns:
    if is_valid(pattern, 0):
        count += 1

print(count)
