import z3

input = open(0).read().strip().split("\n")

solver = z3.Solver()

# The equations I need are:
# sx, sy, sz
# svx, svy, svz

# Each equation +1 unknown time t, should only need 3 since 9 unknowns and 9 eqns
# x1 + t1 * vx1 = sx + t1 * svx
# etc for the y and z
# x2 + t2 * vx2 = sx + t2 * svx
# x3 + t3 * vx3 = sx + t3 * svx

times = [z3.Int(f"t{num}") for num in range(1, 4)]
starting_positions = z3.Ints("spx spy spz")
spx, spy, spz = starting_positions
starting_velocities = z3.Ints("svx svy svz")
svx, svy, svz = starting_velocities

solver.add([time >= 0 for time in times])
solver.add([vel <= 250 for vel in starting_velocities])
solver.add([-250 <= vel for vel in starting_velocities])

for i in range(3):
    position, velocity = input[i].split("@")
    px, py, pz = list(map(int, position.split(",")))
    vx, vy, vz = list(map(int, velocity.split(",")))

    solver.add(px + times[i] * vx == spx + times[i] * svx)
    solver.add(py + times[i] * vy == spy + times[i] * svy)
    solver.add(pz + times[i] * vz == spz + times[i] * svz)

ans = None
if solver.check() == z3.sat:
    model = solver.model()
    ans = sum(model[pos].as_long() for pos in starting_positions)
else:
    print(":(")

print(ans)
