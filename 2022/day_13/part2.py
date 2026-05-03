import json
from functools import cmp_to_key

input = [json.loads(line) for line in open(0).read().strip().split()]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if (test := compare(left[i], right[i])) != 0:
                return test
        if len(left) != len(right):
            return len(left) - len(right)
        return 0
    else:
        assert False

input.append([[2]])
input.append([[6]])
input.sort(key=cmp_to_key(compare))

two, six = -1, -1
for indice, item in enumerate(input):
    if item == [[2]]:
        two = indice + 1
    if item == [[6]]:
        six = indice + 1

print(two * six)
