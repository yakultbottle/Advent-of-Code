coords = [tuple(map(int, row.split(","))) for row in open(0).read().strip().split("\n")]

def rect_area(one: tuple[int, int], two: tuple[int, int]) -> int:
    first = abs(one[0] - two[0]) + 1
    second = abs(one[1] - two[1]) + 1
    return first * second

n = len(coords)
maxArea = -1
for i in range(n):
    for j in range(i + 1, n):
        area = rect_area(coords[i], coords[j])
        maxArea = max(maxArea, area)
print(maxArea)
