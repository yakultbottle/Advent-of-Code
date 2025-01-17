import sys
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

'''
XOR of current pair = curr_xor
carry_in = prev_carry_in | re_carry
re_carry = curr_xor & prev_prev_carry_in ...?

sum = carry_in ^ curr_xor
carry_out = carry_in | prev_carry_in
'''

formulas = {}
while queue:
    string = queue.pop()
    in1, operation, in2, _, out = string.split(" ")

    formulas[out] = (in1, operation, in2)

def make_wire(char: str, num: int) -> str:
    return char + str.rjust(str(num), 2, "0")

def is_sum(wire: str) -> bool:
    if wire not in formulas:
        return False
    if wire[0] != "z":
        return False
    num = int(wire[1:])
    x, op, y = formulas[wire]
    if op != "XOR":
        return False
    if wire == make_wire("z", 0):
        if x == make_wire("x", 0) and y == make_wire("y", 0) or x == make_wire("y", 0) and y == make_wire("x", 0):
            return True
        return False

    return is_xor(y, num) and is_carry_bit(x, num) or is_xor(x, num) and is_carry_bit(y, num)

def is_xor(wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    x, op, y = formulas[wire]
    if op != "XOR":
        # print("is_xor", wire)
        return False
    return x == make_wire("x", num) and y == make_wire("y", num) or x == make_wire("y", num) and y == make_wire("x", num)

def is_carry_bit(wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    x, op, y = formulas[wire]
    if num == 1:
        if op == "AND" and (x == make_wire("x", 0) and y == make_wire("y", 0) or x == make_wire("y", 0) and y == make_wire("x", 0)):
            return True
        return False
    if op != "OR":
        return False
    return is_carry_out(x, num - 1) and is_re_carry(y, num - 1) or is_carry_out(y, num - 1) and is_re_carry(x, num - 1)

def is_carry_out(wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    x, op, y = formulas[wire]
    if op != "AND":
        return False
    return x == make_wire("x", num) and y == make_wire("y", num) or x == make_wire("y", num) and y == make_wire("x", num)

def is_re_carry(wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    x, op, y = formulas[wire]
    if op != "AND":
        return False
    return is_xor(x, num) and is_carry_bit(y, num) or is_xor(y, num) and is_carry_bit(x, num)

def verify(i: int) -> bool:
    wire = make_wire("z", i)
    if wire not in formulas:
        return False
    return is_sum(wire)

def progress() -> int:
    for i in range(100):
        if not verify(i):
            return i

    return -1

# print(progress())

output = []
for _ in range(4):
    baseline = progress()

    x, y = "", ""
    for x in formulas:
        for y in formulas:
            if x == y:
                continue

            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    print(x, y)
    output.append(x)
    output.append(y)

output.sort()
answer = ",".join(output)
print(answer)
