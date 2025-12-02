input = open(0).read().strip()

ranges = [tuple(map(int, r.split("-"))) for r in input.split(",")]

def is_valid(num: int) -> bool:
    string = str(num)
    n = len(string)

    if n & 1:
        return False

    return string[:n // 2] == string[n // 2:]

ans = 0
for start, end in ranges:
    for num in range(start, end + 1):
        if is_valid(num):
            ans += num
print(ans)
