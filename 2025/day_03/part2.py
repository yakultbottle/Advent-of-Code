# banks = open(0).read().strip().split("\n")

# def largest(bank: str, start: int, end: int) -> int:
#     maximum = 0
#     index = -1
#     for i in range(start, end):
#         num = int(bank[i])
#         if num > maximum:
#             maximum = num
#             index = i
#     return index

# ans = 0
# for bank in banks:
#     n = len(bank)
#     start = 0
#     maximum = []
#     for i in range(11, -1, -1):
#         index = largest(bank, start, n - i)
#         maximum.append(bank[index])
#         start = index + 1
#     ans += int("".join(maximum))

# print(ans)

# Monotonic stack solution, hoped to be faster but wasn't
banks = [list(map(int, bank)) for bank in open(0).read().strip().split("\n")]
n = len(banks[0])
ans = 0

for bank in banks:
    temp = []
    for idx, num in enumerate(bank):
        while temp and temp[-1] < num and n - idx > 12 - len(temp):
            temp.pop()
        if len(temp) >= 12:
            continue

        temp.append(num)

    something = int("".join([str(x) for x in temp]))
    ans += something
print(ans)
