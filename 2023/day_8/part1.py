import sys
from collections import defaultdict

input = sys.stdin.read().strip()
instructions, nodes = input.split("\n\n")

adj_list = defaultdict(list)
for line in nodes.split("\n"):
    frm, to = line.split(" = ")
    left, right = to[1:4], to[6:9]

    adj_list[frm].append(left)
    adj_list[frm].append(right)

curr = "AAA"

count = 0
while curr != "ZZZ":
    for instruction in instructions:
        if instruction == "L":
            curr = adj_list[curr][0]
        else:
            curr = adj_list[curr][1]
        count += 1

print(count)
