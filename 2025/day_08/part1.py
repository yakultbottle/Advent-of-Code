import math
from collections import Counter
from functools import reduce

boxes = [list(map(int, row.strip().split(","))) for row in open(0).readlines()]

def euclid_dist(one: list[int], two: list[int]) -> float:
    return math.sqrt((one[0] - two[0])**2 + (one[1] - two[1])**2 + (one[2] - two[2])**2)

n = len(boxes)
distances = []
for i in range(n):
    for j in range(i + 1, n):
        dist = (euclid_dist(boxes[i], boxes[j]), i, j)
        distances.append(dist)

distances.sort()

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)

        self.parent[irep] = jrep

unionfind = UnionFind(n)
NUM_UNIONS = 1000
for i in range(NUM_UNIONS):
    _, first, second = distances[i]
    unionfind.union(first, second)

sizes = Counter()
for i in range(n):
    parent = unionfind.find(i)
    sizes[parent] += 1
top_three = [count for element, count in sizes.most_common(3)]
ans = reduce(lambda x, y: x * y, top_three)
print(ans)

