banks = open(0).read().strip().split("\n")

def largest(bank: str, start: int, end: int) -> int:
    maximum = 0
    index = -1
    for i in range(start, end):
        num = int(bank[i])
        if num > maximum:
            maximum = num
            index = i
    return index

ans = 0
for bank in banks:
    n = len(bank)
    start = 0
    maximum = []
    for i in range(11, -1, -1):
        index = largest(bank, start, n - i)
        maximum.append(bank[index])
        start = index + 1
    ans += int("".join(maximum))

print(ans)
