input = open(0).read().strip().split(",")

total = 0
for hash in input:
    count = 0
    for char in hash:
        count += ord(char)
        count *= 17
        count &= 0xFF
    total += count
print(total)
