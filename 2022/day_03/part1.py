input = open(0).read().strip().split("\n")

count = 0
for line in input:
    n = len(line)
    assert n & 1 == 0

    half = n // 2
    seen = set(line[:half])

    shared = '0'
    for char in line[half:]:
        if char in seen:
            shared = char
            break
    assert shared != '0'

    offset = ord('a') - 1 if shared.islower() else ord('A') - 1 - 26
    count += ord(shared) - offset

print(count)
