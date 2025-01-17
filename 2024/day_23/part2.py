import sys
from collections import defaultdict

s = sys.stdin.read().strip()

adj_list = defaultdict(set)
for line in s.split("\n"):
    frm, to = tuple(line.split("-"))
    adj_list[frm].add(to)
    adj_list[to].add(frm)

def is_connected(clique: set[str]) -> bool:
    is_ok = True
    for node in clique:
        temp = set()
        temp.add(node)
        for edge in adj_list[node]:
            if edge in clique:
                temp.add(edge)

        if temp != clique:
            is_ok = False

    return is_ok

# Finds the maximum clique given a starting node
def max_clique(clique: set[str], node: str) -> set[str]:
    clique.add(node)
    if not is_connected(clique):
        return set()

    maximum = set(clique)
    maxSoFar = len(clique)

    for edge in adj_list[node]:
        if edge in clique:
            continue
        temp = max_clique(clique, edge)
        if not temp:
            clique.remove(edge)
        if len(temp) > maxSoFar:
            maximum = temp
            maxSoFar = len(temp)
    
    return maximum

def post_process(computers: list[str]) -> str:
    return ",".join(sorted(computers))

maxSoFar = 0
computers = set()
for node in adj_list:
    maximum = max_clique(set(), node)
    if len(maximum) > maxSoFar:
        computers = maximum
        maxSoFar = len(maximum)

output = post_process(list(computers))
print(output)
