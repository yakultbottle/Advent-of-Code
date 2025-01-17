import sys
from functools import cache

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

def rob2_path(pos: tuple[int,int], dir: str) -> str:
    next_loc = dpad[dir]
    diff = calc_diff(pos, next_loc)

    x, y = diff

    dx = ">" if x > 0 else "<"
    dy = "v" if y > 0 else "^"

    move_x_first = False
    if x < 0:
        if pos[1] == 0 and (pos[0] + x == 0):
            move_x_first = False
        else:
            move_x_first = True
    elif y < 0:
        if pos[0] == 0 and (pos[1] + y == 0):
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

    return "".join(string)

@cache
def calc_len(pos: tuple[int,int], path: str, depth: int) -> int:
    if depth == 1:
        count = 0
        start = pos
        output = ""
        for char in path:
            next_path = rob2_path(start, char)
            output += next_path
            start = dpad[char]
            count += len(next_path)
        return count

    count = 0
    start = pos
    for char in path:
        next_path = rob2_path(start, char)
        count += calc_len(pos, next_path, depth - 1)
        start = dpad[char]
    return count

# Main code
codes = [code.strip() for code in sys.stdin.readlines()]

count = 0
for code in codes:
    rob1_pos = numpad["A"]
    path1 = []
    for letter in code:
        path1.append(rob1_path(letter))
    path1 = "".join(path1)

    depth = 25
    pos = dpad["A"]
    output = calc_len(pos, path1, depth)

    num_part = int(code[:-1])
    complexity = output * num_part
    count += complexity

print(count)
