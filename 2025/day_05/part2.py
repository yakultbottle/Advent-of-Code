ranges, _ = [item.split("\n") for item in open(0).read().strip().split("\n\n")]

sorted_ranges = []
for r in ranges:
    start, end = map(int, r.split("-"))
    sorted_ranges.append((start, end))

sorted_ranges.sort()

idx = 1
n = len(sorted_ranges)
while idx < len(sorted_ranges):
    first = sorted_ranges[idx - 1]
    second = sorted_ranges[idx]

    if first[1] >= second[0]:
        debug = sorted_ranges.pop(idx - 1)
        sorted_ranges[idx - 1] = (min(first[0], second[0]), max(first[1], second[1]))
    else:
        idx += 1

count = 0
for start, end in sorted_ranges:
    count += (end - start) + 1
print(count)
