from itertools import combinations
from collections import defaultdict

input = open(0).read().strip().split("\n")

def find_parity(switch: tuple[int, ...]) -> int:
    return sum(1 << i for i, num in enumerate(switch) if num & 1)

def generate_all_patterns(switches: tuple[tuple[int, ...], ...], joltages: tuple[int, ...]) -> defaultdict[int, list[tuple[tuple[int, ...], int]]]:
    results: defaultdict[int, list[tuple[tuple[int, ...], int]]] = defaultdict(list)

    for r in range(len(switches) + 1):
        for combi in combinations(switches, r):
            total_cost = [0 for _ in range(len(joltages))]

            for switch in combi:
                for num in switch:
                    total_cost[num] += 1

            parity_pattern = find_parity(tuple(total_cost))
            results[parity_pattern].append((tuple(total_cost), len(combi)))

    return results

def num_presses(switches: tuple[tuple[int, ...], ...], joltages: tuple[int, ...]) -> int:
    patterns = generate_all_patterns(switches, joltages)

    memo = {}
    def recurse(target: tuple[int, ...]) -> int:
        if target in memo:
            return memo[target]

        if all(num == 0 for num in target):
            return 0

        parity_pattern = find_parity(target)

        minimum = float('inf')
        for presses, count in patterns[parity_pattern]:
            if any(i < j for i, j in zip(target, presses)):
                continue
            new_target = tuple((i - j) // 2 for i, j in zip(target, presses))
            minimum = min(minimum, 2 * recurse(new_target) + count)

        memo[target] = minimum
        return minimum

    return recurse(joltages)

ans = 0
for row in input:
    _, *second, third = row.split()
    switches = tuple(tuple(map(int, switch[1:-1].split(","))) for switch in second)
    end_joltages = tuple(int(num) for num in third[1:-1].split(","))

    memo = {}
    ans += num_presses(switches, end_joltages)

print(ans)
