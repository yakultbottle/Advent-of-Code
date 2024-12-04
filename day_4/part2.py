import sys

def read_data() -> list[str]:
    input_lines = sys.stdin.read().strip().splitlines()
    return input_lines

def is_in_bounds(board:list[str], x: int, y:int) -> bool:
    if x >= len(board[0]) or x < 0:
        return False
    if y >= len(board) or y < 0:
        return False
    return True

'''
x = 1, -1, -1, 1
y = -1, -1, 1, 1
'''

def main(board: list[str]) -> int:
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 'A':
                continue

            string = ""
            for direction in range(4):
                x_dir = 1 if direction == 0 or direction == 3 else -1
                y_dir = 1 if direction >= 2 else -1
                # print(f"{direction}: ({x_dir}, {y_dir})")

                new_x = j + x_dir
                new_y = i + y_dir
                if is_in_bounds(board, new_x, new_y):
                    string += board[new_y][new_x]

            # GPT improvement: valid_patterns = {"SMMS", "MMSS", "MSSM", "SSMM"}
            # then check if string in valid_patterns
            if string == "SMMS" or string == "MMSS" or string == "MSSM" or string == "SSMM":
                # print(f"{j}, {i}: direction {direction}")
                count += 1
    
    return count

'''
GPT improvement to check all permutations in a specified order:

from collections import deque

# Generate all rotations of the base pattern
base_pattern = "SMMS"
rotations = set()
deque_pattern = deque(base_pattern)

for _ in range(len(base_pattern)):
    rotations.add("".join(deque_pattern))
    deque_pattern.rotate(1)

if string in rotations:
    # Found a match
'''

if __name__ == "__main__":
    board = read_data()
    output = main(board)
    print(output)
