import sys
from collections import defaultdict

modulo = 0xFFFFFF # 2^24

pricelog = defaultdict(int)
def find_secret(secret: int, depth: int):
    next_secret = secret
    prices = []
    differences = []
    
    for _ in range(depth):
        prices.append(next_secret % 10)

        next_secret ^= (next_secret << 6) # * 64
        next_secret &= modulo
        next_secret ^= (next_secret >> 5) # / 32
        next_secret &= modulo
        next_secret ^= (next_secret << 11) # * 2048
        next_secret &= modulo

    for i in range(len(prices) - 1):
        differences.append(prices[i + 1] - prices[i])

    left = 0
    right = left + 4

    seen = set()
    while right <= len(differences):
        sequence = tuple(differences[left:right])
        if sequence in seen:
            left += 1
            right += 1
            continue
        seen.add(sequence)
        pricelog[sequence] += prices[right]
        left += 1
        right += 1

    return

input = list(map(int, sys.stdin.read().splitlines()))
 
depth = 2000
count = 0
for secret in input:
    find_secret(secret, depth)
    count += 1

maxPrice = 0
for sequence, price in pricelog.items():
    if price > maxPrice:
        maxPrice = price
        maxSequence = sequence

print(maxSequence, maxPrice)
