import sys
from functools import cmp_to_key
from collections import defaultdict

input = sys.stdin.read().strip()

hands = []
for line in input.split("\n"):
    hand, bid = line.split()
    bid = int(bid)
    hand = (hand, bid)
    hands.append(hand)

ordering = {
    "A" : 0,
    "K" : 1,
    "Q" : 2,
    "J" : 3,
    "T" : 4,
    "9" : 5,
    "8" : 6,
    "7" : 7,
    "6" : 8,
    "5" : 9,
    "4" : 10,
    "3" : 11,
    "2" : 12
}

def lexico_cmp(a: str, b: str) -> int:
    for i in range(len(a)):
        if a[i] == b[i]:
            continue

        return ordering[a[i]] - ordering[b[i]]
    print("oh no")
    return 0

def cmp(x: tuple[str,int], y: tuple[str,int]) -> int:
    # return negative if x < y, 0 if x == y, and positive if x > y
    a, b = x[0], y[0]

    if a == b:
        print("explode")
        return 0

    freq_a = defaultdict(int)
    freq_b = defaultdict(int)
    for i in range(len(a)):
        freq_a[a[i]] += 1
        freq_b[b[i]] += 1

    if len(freq_a) > len(freq_b):
        return 1
    elif len(freq_a) < len(freq_b):
        return -1

    counts_a = sorted(freq_a.values())
    counts_b = sorted(freq_b.values())

    if len(freq_a) == 2:
        if counts_a == [1, 4]:
            if counts_b == [1, 4]:
                return lexico_cmp(a, b)
            return -1
        elif counts_a == [2, 3]:
            if counts_b == [2, 3]:
                return lexico_cmp(a, b)
            return 1
    
    elif len(freq_a) == 3:
        if counts_a == [1, 2, 2]:
            if counts_b == [1, 2, 2]:
                return lexico_cmp(a, b)
            return 1
        elif counts_a == [1, 1, 3]:
            if counts_b == [1, 1, 3]:
                return lexico_cmp(a, b)
            return -1
    
    return lexico_cmp(a, b)

hands = sorted(hands, key=cmp_to_key(cmp), reverse=True)

count = 1
output = 0
for cards, bid in hands:
    output += bid * count
    count += 1

print(output)
