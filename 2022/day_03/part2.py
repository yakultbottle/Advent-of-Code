input = open(0).read().strip().split("\n")

count = 0
i = 0
for i in range(0, len(input), 3):
    seen1 = set(input[i])
    seen2 = set(input[i + 1])
    seen3 = set(input[i + 2])

    shared = seen1.intersection(seen2).intersection(seen3)
    assert len(shared) == 1
    shared = shared.pop()

    offset = ord('a') - 1 if shared.islower() else ord('A') - 1 - 26
    count += ord(shared) - offset

print(count)
