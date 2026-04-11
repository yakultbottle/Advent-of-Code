boxes, instructions = open(0).read().split("\n\n")
instructions = instructions.strip()

boxes = boxes.split("\n")
nums = boxes.pop()
num_stacks = max(list(map(int, nums.split())))

boxes.reverse()
stack = [list() for _ in range(num_stacks)]

for box in boxes:
    for i, idx in enumerate(range(1, 4 * num_stacks - 2, 4)):
        if idx >= len(box):
            break

        if box[idx] == " ":
            continue

        stack[i].append(box[idx])

for line in instructions.split("\n"):
    _, num, _, src, _, dest = line.split()
    num = int(num)
    src = int(src) - 1
    dest = int(dest) - 1

    temp = []
    for _ in range(num):
        temp.append(stack[src].pop())
    for _ in range(num):
        stack[dest].append(temp.pop())

ans = []
for stk in stack:
    ans.append(stk.pop())
print("".join(ans))

