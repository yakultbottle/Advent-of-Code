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
    "T" : 3,
    "9" : 4,
    "8" : 5,
    "7" : 6,
    "6" : 7,
    "5" : 8,
    "4" : 9,
    "3" : 10,
    "2" : 11,

    "J" : 12
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
    a_jokers = 0
    b_jokers = 0
    for i in range(len(a)):
        if a[i] == "J":
            a_jokers += 1
        else:
            freq_a[a[i]] += 1

        if b[i] == "J":
            b_jokers += 1
        else:
            freq_b[b[i]] += 1

    if a_jokers == 5:
        counts_a = [5]
    else:
        freq_a = sorted(freq_a.items(), key=lambda freq: freq[1])
        freq_a[-1] = (freq_a[-1][0], freq_a[-1][1] + a_jokers)
        counts_a = [value[1] for value in freq_a]

    if b_jokers == 5:
        counts_b = [5]
    else:
        freq_b = sorted(freq_b.items(), key=lambda freq: freq[1])
        freq_b[-1] = (freq_b[-1][0], freq_b[-1][1] + b_jokers)
        counts_b = [value[1] for value in freq_b]

    if len(counts_a) > len(counts_b):
        return 1
    elif len(counts_a) < len(counts_b):
        return -1

    if len(freq_a) == 2:
        if counts_a == [1, 4]:
            if counts_b == [1, 4]:
                return lexico_cmp(a, b)
            return -1
        elif counts_a == [2, 3]:
            if counts_b == [2, 3]:
                return lexico_cmp(a, b)
            return 1
        else:
            print("somethings wrong")
            return 0
    
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
