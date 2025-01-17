import sys

# constants
A = 0
B = 1
C = 2

register = []
def read_data() -> list[int]:
    regs, instructions = sys.stdin.read().split("\n\n")
    for reg in regs.split("\n"):
        register.append(int(reg[12:].strip()))

    instructions = [int(num) for num in instructions[9:].strip().split(",")]
    return instructions

def main(instructions: list[int]) -> list[str]:
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
            out.append(str(combo_operand % 8))
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

if __name__ == "__main__":
    instructions = read_data()
    output = main(instructions)
    print(",".join(output))
