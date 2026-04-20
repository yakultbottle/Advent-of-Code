input = open(0).read().strip().splitlines()

register = 1
instruction = 0
cycle = 1
is_executing = False
pipeline = []
total = 0

while instruction < len(input):
    if (cycle - 20) % 40 == 0:
        total += register * cycle

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

print(total)
