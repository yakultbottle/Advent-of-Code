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
Imagine I want x to follow a pattern of 1, 0, -1, 0 and then repeat. can I do that
in a for loop that goes 0 -> 3?

for loop that goes 0 -> 7
The real problem wants x to go 1, 1, 0, -1, -1, -1, 0, 1
                       y to go 0, -1, -1, -1, 0, 1, 1, 1
'''

def main(board: list[str]) -> int:
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 'X':
                continue

            # Now need to handle all 8 directions
            for direction in range(8):
                x_dir = 0 if (direction + 6) % 4 == 0 else (-1 if (direction + 6) > 8 and (direction + 6) < 12 else 1)
                y_dir = 0 if direction % 4 == 0 else (-1 if direction < 4 else 1)
                # print(f"{direction}: ({x_dir}, {y_dir})")
                string = ""
                for length in range(4):
                    new_x = j + x_dir * length
                    new_y = i + y_dir * length
                    if is_in_bounds(board, new_x, new_y):
                        string += board[new_y][new_x]
                    else:
                        break
                if string == "XMAS":
                    # print(f"{j}, {i}: direction {direction}")
                    count += 1
    
    return count

if __name__ == "__main__":
    board = read_data()
    output = main(board)
    print(output)
