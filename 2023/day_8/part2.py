import sys
from collections import defaultdict

input = sys.stdin.read().strip()
instructions, nodes = input.split("\n\n")

adj_list = defaultdict(list)
starting_points = []

for line in nodes.split("\n"):
    frm, to = line.split(" = ")
    left, right = to[1:4], to[6:9]

    adj_list[frm].append(left)
    adj_list[frm].append(right)

    if frm[2] == "A":
        starting_points.append(frm)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

answer = 1
while starting_points:
    count = 0
    curr = starting_points.pop()

    while curr[2] != "Z":
        for instruction in instructions:
            if curr[2] == "Z":
                break

            if instruction == "L":
                curr = adj_list[curr][0]
            else:
                curr = adj_list[curr][1]
            count += 1

    answer = lcm(answer, count)

print(answer)
