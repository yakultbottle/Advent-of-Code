input = open(0).read().splitlines()

count = 0
for line in input:
    left, right = line.split(",")
    left = list(map(int, left.split("-")))
    right = list(map(int, right.split("-")))

    if (
        left[0] <= right[0] and left[1] >= right[0]
        or right[0] <= left[0] and right[1] >= left[0]
    ):
        count += 1

print(count)
