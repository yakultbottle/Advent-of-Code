import sys
from collections import deque

# constants
A = 0
B = 1
C = 2

register = []
instructions = []
def read_data():
    regs, insts = sys.stdin.read().split("\n\n")
    for reg in regs.split("\n"):
        register.append(int(reg[12:].strip()))

    # instructions = [int(num) for num in instructions[9:].strip().split(",")]
    for num in insts[9:].strip().split(","):
        instructions.append(int(num))

def simulate(i: int) -> list[int]:
    global register
    register = [0, 0, 0]
    register[A] = i

    idx = 0
    length = len(instructions)
    out = []
    
    while idx + 1 < length:
        opcode = instructions[idx]
        lit_operand = instructions[idx + 1]
        combo_operand = lit_operand if lit_operand <= 3 or lit_operand == 7 else register[lit_operand - 4]

        if opcode == 0:
            register[A] >>= combo_operand
        elif opcode == 1:
            register[B] ^= lit_operand
        elif opcode == 2:
            register[B] = combo_operand % 8
        elif opcode == 3:
            if register[A] != 0:
                idx = lit_operand
                continue
        elif opcode == 4:
            register[B] ^= register[C]
        elif opcode == 5:
            out.append(combo_operand % 8)
        elif opcode == 6:
            numerator = register[A]
            denominator = 2 ** combo_operand
            register[B] = numerator // denominator
        elif opcode == 7:
            numerator = register[A]
            denominator = 2 ** combo_operand
            register[C] = numerator // denominator

        idx += 2

    return out

def main() -> int:
    '''
    Based on below code, pattern seems to be that I should match backwards. 
    ie starting from last index. Then for all matches, simply x2 to find all candidates(?)

    global register
    for i in range(1025):
        register = [0, 0, 0]
        register[A] = i
        print(f"{i}: {simulate(instructions)}")
    '''

    global instructions
    candidates = deque([])
    candidates.appendleft(0)

    while candidates:
        start_idx = candidates.pop()
        for i in range(8):
            idx = start_idx + i
            if idx == 0:
                continue
            candidate = simulate(idx)
            length = len(candidate)
            if length > len(instructions):
                break
            if instructions == candidate:
                return idx
            if instructions[-length:] == candidate:
                candidates.appendleft(idx << 3)

    return -1

if __name__ == "__main__":
    read_data()
    output = main()
    '''
    output = simulate(109685330781408)
    print(output)
    output = simulate(109685330781407)
    '''
    print(output)
