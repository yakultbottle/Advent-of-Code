import sys

def read_data() -> list[list[str]]:
    input = sys.stdin.readlines()
    map = [list(line.strip()) for line in input]
    return map

def print_board(board: list[list[str]]):
    for row in board:
        output = ""
        for tile in row:
            output += tile
        print(output)

'''
def main(map: list[list[str]]) -> int:
    guard = (0, 0)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                map[i][j] = "X"
                guard = (j, i)

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    curr_direction = 0

    visited = set()
    count = 0

    finish = False
    while not finish:
        x, y = guard

        while True:
            dx, dy = directions[curr_direction]
            newX = x + dx
            newY = y + dy

            if not (0 <= newX and newX < len(map[0]) and 0 <= newY and newY < len(map)):
                finish = True
                break

            if map[newY][newX] == "#":
                curr_direction = (curr_direction + 1) % 4
                continue

            if_direction = (curr_direction + 1) % 4
            temp_x = x
            temp_y = y
            is_stuck = set()

            if_go_forward_state = ((newX, newY), (dx, dy))
            i = 1
            while True:
                right_dx, right_dy = directions[if_direction]

                right_x = temp_x + right_dx * i
                right_y = temp_y + right_dy * i

                new_if_go_forward_state = ((right_x, right_y), (right_dx, right_dy))

                if not (0 <= right_x and right_x < len(map[0]) and 0 <= right_y and right_y < len(map)):
                    break

                if new_if_go_forward_state in is_stuck:
                    print(new_if_go_forward_state)
                    break

                is_stuck.add(new_if_go_forward_state)

                if map[right_y][right_x] == "#":
                    if_direction = (if_direction + 1) % 4
                    temp_x = temp_x + right_dx * (i - 1)
                    temp_y = temp_y + right_dy * (i - 1)
                    i = 1
                    continue

                if_turn_right_state = ((right_x, right_y), (right_dx, right_dy))

                if if_turn_right_state in visited:
                    # print(if_go_forward_state)
                    # print(if_turn_right_state)
                    # print()
                    count += 1
                    break

                i += 1

            visited.add(if_go_forward_state)

            guard = (newX, newY)
            break

    return count
'''

def main(map: list[list[str]]) -> int:
    # Find the guard's starting position
    guard = (0, 0)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                guard = (j, i)
                break
    
    # Possible directions: Up, Right, Down, Left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    height, width = len(map), len(map[0])
    count = 0

    # Try placing an obstacle at every empty cell
    for obstacle_y in range(height):
        for obstacle_x in range(width):
            if map[obstacle_y][obstacle_x] == '#':
                continue  # Skip existing walls

            # Create a copy of the map and place the obstacle
            test_map = [row[:] for row in map]
            test_map[obstacle_y][obstacle_x] = '#'

            # Simulate guard's path
            if check_infinite_loop(test_map, guard):
                count += 1

    return count

def check_infinite_loop(map, start_pos):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    height, width = len(map), len(map[0])
    
    def simulate_guard():
        curr_pos = start_pos
        curr_direction = 0
        visited_states = set()

        while True:
            x, y = curr_pos
            dx, dy = directions[curr_direction]
            new_x, new_y = x + dx, y + dy

            # Out of bounds check
            if not (0 <= new_x < width and 0 <= new_y < height):
                return False

            # Hit a wall, turn right
            if map[new_y][new_x] == '#':
                curr_direction = (curr_direction + 1) % 4
                continue

            # Track state
            state = (new_x, new_y, curr_direction)
            if state in visited_states:
                return True  # Infinite loop detected
            
            visited_states.add(state)
            curr_pos = (new_x, new_y)

    return simulate_guard()

if __name__ == "__main__":
    map = read_data()
    output = main(map)
    print(output)
