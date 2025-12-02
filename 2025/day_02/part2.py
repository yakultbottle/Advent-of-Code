input = open(0).read().strip()
ranges = [tuple(map(int, r.split("-"))) for r in input.split(",")]

def is_valid(num: int) -> bool:
    string = str(num)
    n = len(string)

    for divisor in divisor_gen(n):
        if is_valider(string, divisor, n):
            return True
    return False

memo = {}
def divisor_gen(n: int) -> list[int]:
    if n in memo:
        return memo[n]

    ans = []
    for i in range(2, n + 1):
        if n % i == 0:
            ans.append(i)
    memo[n] = ans
    return ans

def is_valider(string: str, divisor: int, n: int) -> bool:
    step = n // divisor
    start = 0
    while start + step < n:
        if string[start:start + step] != string[start + step: start + step + step]:
            return False
        start += step
    return True

ans = 0
for start, end in ranges:
    for num in range(start, end + 1):
        if is_valid(num):
            ans += num
print(ans)
