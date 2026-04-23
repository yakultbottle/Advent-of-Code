import re
from collections import deque

input = open(0).read().strip().split("\n\n")

worry_lists = []
operations = []
tests = []
trues = []
falses = []
for i, monkey in enumerate(input):
    _, worries, operation, test, true, false = monkey.split("\n")
    worry_lists.append(deque(map(int, re.findall(r"\d+", worries))))
    operations.append(operation.split()[-3:])
    tests.append(int(re.findall(r"\d+", test)[0]))
    trues.append(int(re.findall(r"\d+", true)[0]))
    falses.append(int(re.findall(r"\d+", false)[0]))

activity = [0] * len(input)
for _ in range(20):
    for i in range(len(input)):
        while worry_lists[i]:
            old = worry_lists[i][0]
            new = eval(" ".join(operations[i]))

            new //= 3

            if new % tests[i] == 0:
                worry_lists[trues[i]].append(new)
            else:
                worry_lists[falses[i]].append(new)

            worry_lists[i].popleft()
            activity[i] += 1

activity.sort()
print(activity[-1] * activity[-2])
