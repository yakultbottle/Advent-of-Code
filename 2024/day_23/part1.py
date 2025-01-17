import sys
import re
from collections import defaultdict

s = sys.stdin.read().strip()

adj_list = defaultdict(set)
for line in s.split("\n"):
    frm, to = tuple(line.split("-"))
    adj_list[frm].add(to)
    adj_list[to].add(frm)

seen = set()
def num_cliques(value: str) -> int:
    temp_seen = set()
    values = adj_list[value]

    for v in seen:
        if v in values:
            values.remove(v)

    count = 0
    for first in values:
        for second in values:
            if first == second:
                continue
            if second in temp_seen:
                continue
            if second in adj_list[first]:
                count += 1
        temp_seen.add(first)
    seen.add(value)
    return count

count = 0
for value in adj_list:
    if re.match("t.", value):
        count += num_cliques(value)

print(count)
