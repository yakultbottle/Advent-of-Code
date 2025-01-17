import sys
# from collections import defaultdict
from collections import deque

s = sys.stdin.read()
inputs, gates = s.split("\n\n")

wires = {}
for line in inputs.strip().split("\n"):
    input, value = line.split(": ")
    wires[input] = int(value)

queue = deque()
for line in gates.strip().split("\n"):
    queue.appendleft(line.strip())

while queue:
    string = queue.pop()
    in1, operation, in2, _, out = string.split(" ")

    if in1 not in wires or in2 not in wires:
        queue.appendleft(string)
        continue
    
    if operation == "OR":
        wires[out] = wires[in1] | wires[in2]
    elif operation == "AND":
        wires[out] = wires[in1] & wires[in2]
    elif operation == "XOR":
        wires[out] = wires[in1] ^ wires[in2]

output = 0
for wire in wires:
    if wire[0] != "z":
        continue
    
    position = int(wire[1:])
    output += wires[wire] << position
print(output)
