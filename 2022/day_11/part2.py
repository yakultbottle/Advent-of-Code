import re
from collections import deque
from functools import reduce

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

all_tests = reduce(lambda x, y: x * y, tests)

activity = [0] * len(input)
for _ in range(10000):
    for i in range(len(input)):
        while worry_lists[i]:
            old = worry_lists[i][0]

            operator, op2 = operations[i][1], operations[i][2]
            val2 = old if op2 == "old" else int(op2)

            if operator == "*":
                new = old * val2
            elif operator == "+":
                new = old + val2
            else:
                new = None
                print("dead")

            if new % tests[i] == 0:
                worry_lists[trues[i]].append(new % all_tests)
            else:
                worry_lists[falses[i]].append(new % all_tests)

            worry_lists[i].popleft()
            activity[i] += 1

activity.sort()
print(activity[-1] * activity[-2])
