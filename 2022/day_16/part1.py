from collections import deque

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

opened = set()

def dfs(curr, time, rate, released):
    if time == 0:
        return released

    maximum = 0
    ok = False

    for nxt, cost in paths[curr]:
        if nxt not in opened and time >= cost + 1:
            ok = True
            opened.add(nxt)
            maximum = max(maximum, dfs(nxt, time - (cost + 1), rate + adj_list[nxt][0], released + rate * (cost + 1)))
            opened.remove(nxt)

    if not ok:
        return released + rate * time

    return maximum

ans = dfs("AA", 30, 0, 0)
print(ans)
