from __future__ import annotations

input = open(0).read().strip().splitlines()

class Node:
    hash_map = {}
    total = 0

    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.size = 0
        self.cached = False

        Node.hash_map[name] = self

    @staticmethod
    def get(name: str) -> Node:
        if name in Node.hash_map:
            return Node.hash_map[name]
        return Node(name)

    def add_child(self, child: Node):
        self.children.append(child)

    def add_size(self, size: int):
        self.size += size

    def total_size(self):
        if self.cached:
            return self.size

        self.cached = True
        self.size = self.size + sum(child.total_size() for child in self.children)

        if self.size <= 100000:
            # print("hi")
            Node.total += self.size
            # print(" ", self.size)

        return self.size

    def __repr__(self):
        return f"{self.name} with children:\n {self.children}"

root = Node("")
path = []
curr_size = 0
for line in input:
    left, *right = line.split()

    if left == "$":
        curr_size = 0
        if right[0] == "cd":
            if right[1] == "..":
                path.pop()
            else:
                path.append(right[1] if right[1] != "/" else "")
    else:
        if left == "dir":
            path.append(right[0])
            node = Node.get("/".join(path))
            path.pop()
            parent = Node.get("/".join(path))
            parent.add_child(node)
        else:
            node = Node.get("/".join(path))
            node.add_size(int(left))

root.total_size()
print(Node.total)
