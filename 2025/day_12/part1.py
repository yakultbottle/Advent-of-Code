*shapes, grids = open(0).read().split("\n\n")

shape_sizes = [sum(1 for char in shape if char == "#") for shape in shapes]

count = 0
for grid in grids.splitlines():
    dimensions, *num_shapes = grid.split()
    num_shapes = list(map(int, num_shapes))
    dimensions = tuple(map(int, dimensions[:-1].split("x")))

    total_area = dimensions[0] * dimensions[1]
    shapes_area = sum(a * b for a, b in zip(shape_sizes, num_shapes))

    if total_area - shapes_area > 0:
        count += 1
print(count)
