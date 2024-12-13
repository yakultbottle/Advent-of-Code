import sys

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

def dfs(target: tuple[int,int], a: tuple[int,int], b: tuple[int,int]) -> int:
    ok = []
    for i in range(100):
        for j in range(100):
            x = i * a[0] + j * b[0]
            y = i * a[1] + j * b[1]
            if (x, y) == target:
                ok.append((i, j))
    
    minSoFar = min((pair[0] * 3 + pair[1] for pair in ok), default=0)
    # print(f"{target}: {minSoFar}")

    return minSoFar

def main(machines: list[tuple[tuple[int,int], tuple[int,int], tuple[int,int]]]) -> int:
    total = 0
    for machine in machines:
        total += dfs(machine[2], machine[0], machine[1])
    return total

if __name__ == "__main__":
    machines = read_data()
    output = main(machines)
    print(output)
