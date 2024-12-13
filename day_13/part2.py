import sys
import numpy as np

def read_data() -> list[tuple[tuple[int,int], tuple[int,int], tuple[int,int]]]:
    machines = [machine for machine in sys.stdin.read().split("\n\n")]
    input = []
    for machine in machines:
        temp = machine.split("\n")
        button_a = temp[0].split("+")
        a = (int(button_a[1][:-3]), int(button_a[2]))

        button_b = temp[1].split("+")
        b = (int(button_b[1][:-3]), int(button_b[2]))

        prize = temp[2].split("=")
        target = (int(prize[1][:-3]), int(prize[2]))
        input.append((a, b, target))

    return input

def solve(target: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
    # Trying to solve Ax = t, where A is [a b] and t is the target matrix
    A = np.array([[a[0], b[0]], [a[1], b[1]]])
    t = np.array([target[0], target[1]])
    
    try:
        x = np.linalg.solve(A, t)
        x_int = np.round(x).astype(int)

        reconstructed_target = A @ x_int

        # Basically checks if solution was an integer solution
        if np.array_equal(reconstructed_target, t):
            return 3 * x_int[0] + x_int[1]

        return 0
    
    # No solution
    except np.linalg.LinAlgError:
        return 0

def main(machines: list[tuple[tuple[int,int], tuple[int,int], tuple[int,int]]]) -> int:
    total = 0
    offset = 10000000000000
    for machine in machines:
        target = (machine[2][0] + offset, machine[2][1] + offset)
        total += solve(target, machine[0], machine[1])
    return total

if __name__ == "__main__":
    machines = read_data()
    output = main(machines)
    print(output)
