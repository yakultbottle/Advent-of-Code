import z3

input = open(0).read().strip().split("\n")

ans = 0
for row in input:
    _, *second, third = row.split()
    switches = [list(map(int, switch[1:-1].split(","))) for switch in second]
    end_joltages = tuple(int(num) for num in third[1:-1].split(","))

    num_lights = len(end_joltages)
    num_switches = len(switches)

    solver = z3.Optimize()
    vars = [z3.Int(f"x{var}") for var in range(num_switches)]

    solver.add([var >= 0 for var in vars])

    for i in range(num_lights):
        terms = []
        for idx, switch in enumerate(switches):
            if any([s == i for s in switch]):
                terms.append(vars[idx])

        solver.add(z3.Sum(terms) == end_joltages[i])

    solver.minimize(sum(vars))

    if solver.check() == z3.sat:
        m = solver.model()
        ans += sum([m[xi].as_long() for xi in vars])
    else:
        print("No solution exists")

print(ans)
