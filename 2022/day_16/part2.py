from collections import deque, defaultdict

input = open(0).read().strip().split("\n")

adj_list = {}
time_left = 30

for line in input:
    left, right = line.split(";")
    start = left.split()[1]
    flow_rate = int(left.split("=")[-1])
    nxt = [dest[-2:] for dest in right.split(",")]

    adj_list[start] = [flow_rate, nxt]

skip = {}
for name, (flow_rate, nxt) in adj_list.items():
    if flow_rate == 0 and name != "AA":
        skip[name] = nxt

paths = {}

for node in adj_list:
    seen = {node: 0}
    frontier = deque([(node, 0)])

    if node in skip:
        continue

    while frontier:
        curr, steps = frontier.popleft()
        _, nxt = adj_list[curr]

        for dest in nxt:
            if dest not in seen:
                seen[dest] = steps + 1
                frontier.append((dest, steps + 1))

    for skippable in skip:
        del seen[skippable]
    if node not in skip:
        del seen[node]
    paths[node] = list(seen.items())

n = len(paths)
opened_idx = {pipe: idx for idx, pipe in enumerate(paths)}
opened = [False for _ in range(n)]

memo = defaultdict(int)

def dfs(curr, time, rate, released):
    key = sum(1 << position for position, valve in enumerate(opened) if valve)
    memo[key] = max(memo[key], released + rate * time)

    if time == 0:
        return released

    maximum = 0
    ok = False

    for nxt, cost in paths[curr]:
        if not opened[opened_idx[nxt]] and time >= cost + 1:
            ok = True
            opened[opened_idx[nxt]] = True
            maximum = max(maximum, dfs(nxt, time - (cost + 1), rate + adj_list[nxt][0], released + rate * (cost + 1)))
            opened[opened_idx[nxt]] = False

    if not ok:
        return released + rate * time

    return maximum


dfs("AA", 26, 0, 0)

all = list(memo.items())

ans = -1
for idx1, (valves1, res1) in enumerate(all):
    for idx2 in range(idx1 + 1, len(all)):
        valves2, res2 = all[idx2]

        if valves1 & valves2:
            continue

        ans = max(ans, res1 + res2)
print(ans)

