import sys

# First Robot
numpad = {
    "7": (0,0), "8": (1,0), "9": (2,0), 
    "4": (0,1), "5": (1,1), "6": (2,1),
    "1": (0,2), "2": (1,2), "3": (2,2),
                "0": (1,3), "A": (2,3)
}

def calc_diff(self: tuple[int,int], other: tuple[int,int]) -> tuple[int,int]:
    return (other[0] - self[0], other[1] - self[1])

def rob1_path(num: str) -> str:
    global rob1_pos
    next_loc = numpad[num]
    diff = calc_diff(rob1_pos, next_loc)

    x, y = diff

    dx = ">" if x > 0 else "<"
    dy = "v" if y > 0 else "^"

    move_x_first = False
    if x < 0:
        if rob1_pos[1] == 3 and (rob1_pos[0] + x == 0):
            move_x_first = False
        else:
            move_x_first = True
    elif y > 0:
        if rob1_pos[0] == 0 and (rob1_pos[1] + y == 3):
            move_x_first = True
        else:
            move_x_first = False

    string = []
    if move_x_first:
        for _ in range(abs(x)):
            string.append(dx)
        for _ in range(abs(y)):
            string.append(dy)
    else:
        for _ in range(abs(y)):
            string.append(dy)
        for _ in range(abs(x)):
            string.append(dx)
    string.append("A")

    rob1_pos = next_loc

    return "".join(string)

# Second Robot
dpad = {
                "^": (1,0), "A": (2,0),
    "<": (0,1), "v": (1,1), ">": (2,1)
}

def rob2_path(dir: str) -> str:
    global rob2_pos
    next_loc = dpad[dir]
    diff = calc_diff(rob2_pos, next_loc)
    # print(rob2_pos, next_loc, diff, sep=" : ")

    x, y = diff

    dx = ">" if x > 0 else "<"
    dy = "v" if y > 0 else "^"

    string = []
    if rob2_pos[1] == 0:
        for _ in range(abs(y)):
            string.append(dy)
        for _ in range(abs(x)):
            string.append(dx)
    else:
        for _ in range(abs(x)):
            string.append(dx)
        for _ in range(abs(y)):
            string.append(dy)
    string.append("A")

    rob2_pos = next_loc

    return "".join(string)

# Main code
codes = [code.strip() for code in sys.stdin.readlines()]

count = 0
for code in codes:
    rob1_pos = numpad["A"]
    path1 = []
    for letter in code:
        path1.append(rob1_path(letter))
    path1 = "".join(path1)
    # print(path1)

    rob2_pos = dpad["A"]

    path2 = []
    for dir in path1:
        path2.append(rob2_path(dir))
    path2 = "".join(path2)
    # print(path2)

    output = []
    for dir in path2:
        output.append(rob2_path(dir))
    output = "".join(output)
    # print(output)

    '''
    print(len(output))
    print(len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"))
    '''
    num_part = int(code[:-1])
    complexity = len(output) * num_part
    '''
    print(len(output), num_part, sep=" * ")
    print(complexity)
    print()
    '''
    count += complexity

print(count)
