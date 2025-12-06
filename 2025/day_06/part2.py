*numbers, operators = open(0).read().splitlines()

count = 0
temp = []
gaps = []
for i in range(len(operators)):
    if operators[i] == " ":
        count += 1
    else:
        if count > 0:
            gaps.append(count)
            count = 0
        temp.append(operators[i])
gaps.append(count + 1)
operators = temp

n = len(numbers)
length = len(numbers[0])
for idx in range(n):
    i = 0
    temp = []
    for gap in gaps:
        temp.append(list(numbers[idx][i:i + gap]))
        i += gap + 1
    numbers[idx] = temp

numbers = [list(col) for col in zip(*numbers)]
for idx in range(len(numbers)):
    numbers[idx] = [list(col) for col in zip(*numbers[idx])]
    for i in range(len(numbers[idx])):
        numbers[idx][i] = "".join(numbers[idx][i]).strip()

def summation(nums: list[str]) -> int:
    count = 0
    for ch in nums:
        if ch == "":
            continue
        count += int(ch)
    return count

def multion(nums: list[str]) -> int:
    count = 1
    for ch in nums:
        if ch == "":
            continue
        count *= int(ch)
    return count

for i, operator in enumerate(operators):
    if operator == "+":
        numbers[i] = summation(numbers[i])
    else:
        numbers[i] = multion(numbers[i])

ans = sum(numbers)
print(ans)
