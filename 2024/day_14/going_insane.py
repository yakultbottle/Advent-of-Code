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

    answer = 0
    maxSoFar = 0
    count = 7055
    if count == 7055:
    # for count in range(7055):
        up_left = 0
        up_right = 0
        down_left = 0
        down_right = 0
        for i in range(len(positions)):
            x = positions[i][0] + velocities[i][0] * count
            x = x % W
            y = positions[i][1] + velocities[i][1] * count
            y = y % H

            if x < W // 2 and y < H // 2:
                up_left += 1
            elif x > W // 2 and y < H // 2:
                up_right += 1
            elif x < W // 2 and y > H // 2:
                down_left += 1
            elif x > W // 2 and y > H // 2:
                down_right += 1

        # product = up_left * up_right * down_left * down_right
        temp = max(max(up_left, up_right), max(down_left, down_right))
        if maxSoFar < temp:
            maxSoFar = temp
            answer = count

        if count == 7055 or count == 86 or count == 31 or count == 34 or count == 51 or count == 386:
            pos_set = set([tuple(x) for x in positions])
            for row in range(H):
                temp = ""
                for col in range(W):
                    if (col, row) in pos_set:
                        temp += "#"
                    else:
                        temp += "."
                print(temp)

            print()

    return answer

if __name__ == "__main__":
    read_data()
    output = main()
    print(output)
