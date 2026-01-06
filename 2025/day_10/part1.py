from itertools import combinations

input = open(0).read().strip().split("\n")

ans = 0
for row in input:
    first, *second, _ = row.split()
    end_state = sum(1 << i for i, char in enumerate(first[1:-1]) if char == "#")
    switches = [sum(1 << i for i in map(int, switch[1:-1].split(","))) for switch in second]

    num = -1
    for r in range(len(switches) + 1):
        for combi in combinations(switches, r):
            curr_state = 0
            for switch in combi:
                curr_state ^= switch

            if curr_state == end_state:
                break
        else:
            continue
        num = r

    if num == -1:
        print("what")

    ans += num

print(ans)
