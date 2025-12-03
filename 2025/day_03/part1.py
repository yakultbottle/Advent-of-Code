banks = open(0).read().strip().split("\n")

ans = 0
for bank in banks:
    left = 0
    maximum = 0
    for right in range(1, len(bank)):
        num_left, num_right = int(bank[left]), int(bank[right])
        num = num_left * 10 + num_right
        maximum = max(num, maximum)
        if num_right > num_left:
            left = right
    ans += maximum
print(ans)
