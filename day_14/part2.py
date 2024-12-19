import sys

robots = []
def read_data():
    input = [line.strip().split(" ") for line in sys.stdin.readlines()]
    
    for i in range(len(input)):
        pos = [int(x) for x in input[i][0][2:].split(",")]
        vel = [int(x) for x in input[i][1][2:].split(",")]
        robots.append((pos,vel))
    return

def main() -> tuple[int,int]:
    H = 103
    W = 101
    min_second = 0
    min_sf = float("inf")

    for second in range(H * W):
        up_left = 0
        up_right = 0
        down_left = 0
        down_right = 0

        if second % 500 == 0:
            print(second)
        for position, velocity in robots:
            posx, posy = position
            velx, vely = velocity

            x = (posx + velx * second) % W
            y = (posy + vely * second) % H

            if x < W // 2 and y < H // 2:
                up_left += 1
            elif x > W // 2 and y < H // 2:
                up_right += 1
            elif x < W // 2 and y > H // 2:
                down_left += 1
            elif x > W // 2 and y > H // 2:
                down_right += 1

        safety_factor = up_left * up_right * down_left * down_right

        if safety_factor < min_sf:
            min_sf = safety_factor
            min_second = second

    return (min_second, min_sf)

if __name__ == "__main__":
    read_data()
    output = main()
    print()
    print(output)
