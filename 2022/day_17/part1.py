jets = open(0).read().strip()

shapes_str = [shape.split("\n") for shape in open("shapes.txt").read().strip().split("\n\n")]
max_width, max_height = max(len(width) for shape in shapes_str for width in shape), max(len(height) for height in shapes_str)

shapes = []
for shape in shapes_str:
    temp = [[False for _ in range(max_width)] for _ in range(max_height)]
    height = len(shape)
    start = max_height - height

    for shape_idx, y in enumerate(range(start, max_height)):
        for x, string in enumerate(shape[shape_idx]):
            if string == "#":
                temp[max_height - y - 1][x] = True

    shapes.append(temp)

heights = [0] * 7
blocks = set()
for i in range(7):
    blocks.add((i, 0))

count = 0
shapes_ptr = 0
shapes_len = len(shapes)
jet_ptr = 0
jet_len = len(jets)

while count < 2022:
    shape = shapes[shapes_ptr]
    shapes_ptr = (shapes_ptr + 1) % shapes_len

    ok = False
    starting_y = max(heights) + 4
    while not ok:
        for row_idx in range(len(shape)):
            curr_y = starting_y + row_idx
            for j, char in enumerate(shape[row_idx]):
                if char and heights[j + 2] > curr_y:
                    ok = False
                    break
            else:
                continue
            break
        else:
            ok = True
            break
        starting_y += 1

    trial_x = 2

    x, y = trial_x, starting_y
    while ok:
        jet = jets[jet_ptr]
        jet_ptr = (jet_ptr + 1) % jet_len

        if jet == ">":
            push = 1
        else:
            push = -1

        x += push
        # check if cannot be pushed
        for y_offset in range(max_height):
            test_y = y + y_offset
            for x_offset in range(max_width):
                test_x = x + x_offset

                if shape[y_offset][x_offset] and (test_x < 0 or test_x >= len(heights) or (test_x, test_y) in blocks):
                    x -= push
                    break
            else:
                continue
            break

        y -= 1
        # check if hit floor
        for y_offset in range(max_height):
            test_y = y + y_offset
            for x_offset in range(max_width):
                test_x = x + x_offset

                if shape[y_offset][x_offset] and (test_x, test_y) in blocks:
                    ok = False
                    break
            else:
                continue
            break
        else:
            continue

        y += 1

        for y_offset in range(max_height):
            test_y = y + y_offset
            for x_offset in range(max_width):
                test_x = x + x_offset

                if shape[y_offset][x_offset]:
                    heights[test_x] = max(heights[test_x], test_y)
                    blocks.add((test_x, test_y))

    count += 1
print(max(heights))
