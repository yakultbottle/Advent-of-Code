*numbers, operators = open(0).read().strip().splitlines()

numbers = [list(map(int, row.split())) for row in numbers]
numbers = [list(col) for col in zip(*numbers)]
operators = operators.split()

def mul(nums: list[int]) -> int:
    count = 1
    for num in nums:
        count *= num
    return count

for i, operator in enumerate(operators):
    if operator == "+":
        numbers[i] = sum(numbers[i])
    else:
        numbers[i] = mul(numbers[i])

ans = sum(numbers)
print(ans)
