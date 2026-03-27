input = open(0).read().strip().split("\n")

n = len(input)

def stone_z_intersect(dx: int, dy: int):
    def parse_line(idx: int):
        position, velocity = input[idx].split("@")
        px, py, pz = list(map(int, position.split(",")))
        vx, vy, vz = list(map(int, velocity.split(",")))
        return ((px, py, pz), (vx + dx, vy + dy, vz))

    (px1, py1, pz1), (vx1, vy1, vz1) = parse_line(0)
    (px2, py2, pz2), (vx2, vy2, vz2) = parse_line(1)

    denominator = vx1 * vy2 - vy1 * vx2

    # Parallel
    if denominator == 0:
        return False

    numerator1 = (vx2 * (py1 - py2) - vy2 * (px1 - px2))
    numerator2 = (vx1 * (py1 - py2) - vy1 * (px1 - px2))

    t1 = numerator1 // denominator
    t2 = numerator2 // denominator

    # Intersection point is negative time
    if t1 < 0 or t2 < 0:
        return False

    # Intersection is non integer
    if t1 * denominator != numerator1 or t2 * denominator != numerator2:
        return False

    start_x = px1 + t1 * vx1
    start_y = py1 + t1 * vy1

    for i in range(2, n):
        (px, py, _), (vx, vy, _) = parse_line(i)

        if vx != 0:
            if (start_x - px) % vx != 0:
                return False
            t = (start_x - px) // vx
        elif vy != 0:
            if (start_y - py) % vy != 0:
                return False
            t = (start_y - py) // vy
        else:
            if px != start_x or py != start_y:
                return False
            return True

        if t < 0:
            return False

        if px + vx * t != start_x or py + vy * t != start_y:
            return False

    z1 = pz1 + vz1 * t1
    z2 = pz2 + vz2 * t2
    dz = (z2 - z1) // (t2 - t1)

    start_z = z1 - dz * t1

    # print(f"Intercept: {start_x}, {start_y}, {start_z}")
    return start_x + start_y + start_z

ans = None
for dx in range(-250, 250):
    for dy in range(-250, 250):
        dz = stone_z_intersect(dx, dy)
        if dz:
            ans = dz
            break
print(ans)

