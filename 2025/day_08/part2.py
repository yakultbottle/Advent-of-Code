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

    def __str__(self):
        return f"UnionFind: {str(self.parent)}"

unionfind = UnionFind(n)
prev = -1
ans = (-1, -1)
for i in range(len(distances)):
    _, first, second = distances[i]
    unionfind.union(first, second)
    for i in range(n):
        parent = unionfind.find(i)
        if parent != prev and prev >= 0:
            prev = -1
            break
        prev = parent
    else:
        # print(boxes[first], boxes[second])
        ans = (first, second)
        break

ans = boxes[first][0] * boxes[second][0]
print(ans)

