import json

input = open(0).read().strip().split("\n\n")

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        elif left < right:
            return True
        else:
            return None
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if (test := compare(left[i], right[i])) is not None:
                return test
        if len(left) != len(right):
            return len(left) <= len(right)
        return None
    else:
        assert 1 == 2

ans = 0
for indice, line in enumerate(input):
    ok = None
    left, right = [json.loads(x) for x in line.split("\n")]

    if compare(left, right):
        ans += (indice + 1)

print(ans)
