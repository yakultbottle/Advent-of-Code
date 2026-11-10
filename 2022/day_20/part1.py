class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val)

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.head.prev = self.tail
        self.original_positions = []
        self.size = 0

    def append(self, val: int):
        node = Node(val=val, next=self.tail, prev=self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        self.original_positions.append(node)
        self.size += 1

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, shift: int, node: Node, curr: Node):
        while shift > 0:
            if curr.next == self.tail:
                curr = self.head
            curr = curr.next
            shift -= 1

        curr.next.prev = node
        node.next = curr.next
        curr.next = node
        node.prev = curr

    def shift(self, index: int):
        node = self.original_positions[index]
        steps = node.val % (self.size - 1)

        if steps == 0:
            return

        prev = node.prev
        self.remove(node)
        self.insert(steps, node, prev)

    def __repr__(self):
        curr = self.head.next
        arr = []
        while curr != self.tail:
            arr.append(curr)
            curr = curr.next
        return str(arr)

input = list(map(int, open(0).read().strip().split("\n")))

dll = DLL()
for i, val in enumerate(input):
    dll.append(val)

for i in range(dll.size):
    dll.shift(i)

curr = dll.head.next
i = 0
arr = []
while curr != dll.tail:
    if curr.val == 0:
        zero = i
    arr.append(curr.val)
    curr = curr.next
    i += 1

ans = 0
for i in range(1, 4):
    value = zero + i * 1000
    ans += arr[value % dll.size]
print(ans)
