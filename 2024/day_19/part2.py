import sys
from collections import defaultdict

towels, patterns  = [thing.strip() for thing in sys.stdin.read().split("\n\n")]

patterns = [pattern.strip() for pattern in patterns.split("\n")]
towels = [towel.strip() for towel in towels.split(", ")]

memo = defaultdict(int)
def num_ways(pattern: str, idx: int) -> int:
    if pattern[idx:] in memo:
        return memo[pattern[idx:]]

    if idx >= len(pattern):
        return 0

    if pattern[idx:] in towels:
        memo[pattern[idx:]] += 1
    
    for towel in towels:
        if pattern[idx:(idx + len(towel))] == towel:
            memo[pattern[idx:]] += num_ways(pattern, idx + len(towel))

    return memo[pattern[idx:]]

count = 0
for pattern in patterns:
    count += num_ways(pattern, 0)

print(count)
