import sys

positions = []
velocities = []
def read_data():
    input = [line.strip().split(" ") for line in sys.stdin.readlines()]
    
    for i in range(len(input)):
        pos = [int(x) for x in input[i][0][2:].split(",")]
        positions.append(pos)
        vel = [int(x) for x in input[i][1][2:].split(",")]
        velocities.append(vel)
    return

def main() -> int:
    H = 7 if len(positions) == 12 else 103
    W = 11 if len(positions) == 12 else 101
    up_left = 0
    up_right = 0
    down_left = 0
    down_right = 0

    for i in range(len(positions)):
        x = positions[i][0] + velocities[i][0] * 100
        x = x % W
        y = positions[i][1] + velocities[i][1] * 100
        y = y % H

        if x < W // 2 and y < H // 2:
            up_left += 1
        elif x > W // 2 and y < H // 2:
            up_right += 1
        elif x < W // 2 and y > H // 2:
            down_left += 1
        elif x > W // 2 and y > H // 2:
            down_right += 1

    return up_left * up_right * down_left * down_right

if __name__ == "__main__":
    read_data()
    output = main()
    print(output)
