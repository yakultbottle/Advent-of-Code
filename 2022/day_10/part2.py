input = open(0).read().strip().splitlines()

register = 1
instruction = 0
cycle = 1
is_executing = False
pipeline = []
total = 0

buffer = ["." for _ in range(40)]

while instruction < len(input):
    pixel = (cycle - 1) % 40

    if abs(register - pixel) <= 1:
        buffer[pixel] = "#"
    else:
        buffer[pixel] = "."

    if cycle > 1 and pixel == 0:
        print("".join(buffer))

    if pipeline:
        register += pipeline.pop()

    if not is_executing:
        if input[instruction] != "noop":
            _, num = input[instruction].split()
            pipeline.append(int(num))
            is_executing = True

        instruction += 1
    else:
        is_executing = False

    cycle += 1

print("".join(buffer))
