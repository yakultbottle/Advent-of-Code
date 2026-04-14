from __future__ import annotations

input = open(0).read().strip().splitlines()

class Node:
    hash_map = {}
    delete = float('inf')

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

    def total_size(self, min_to_delete = float('inf')):
        if self.size > min_to_delete:
            Node.delete = min(Node.delete, self.size)

        self.size = self.size + sum(child.total_size(min_to_delete) for child in self.children)

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

total_size = root.total_size()
space_left = 70000000 - total_size
min_to_delete = 30000000 - space_left

root.total_size(min_to_delete)
print(Node.delete)
