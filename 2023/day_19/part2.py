from collections import defaultdict
from copy import deepcopy
from functools import reduce
from operator import mul

workflows_str, parts = open(0).read().strip().split("\n\n")

def parse_rules(string: str) -> list[tuple[list[str], str]]:
    rules_str = string.split(",")

    rules = []
    for rule_str in rules_str:
        if ':' not in rule_str:
            condition = ['True']
            result = rule_str
        else:
            condition, result = rule_str.split(":")
            condition = [condition[0], condition[1], condition[2:]]
        rules.append((condition, result))
    return rules

workflows = defaultdict(list)
for workflow in workflows_str.split("\n"):
    label, rules = workflow[:-1].split("{")
    workflows[label] = parse_rules(rules)

def consider(range: dict[str, list[int]], condition: list[str], is_negated: bool = False):
    if len(condition) <= 2:
        return range

    var, op, val = condition
    val = int(val)

    if is_negated:
        if op == '>':
            op = '<'
            val += 1
        else:
            op = '>'
            val -= 1

    new_range = deepcopy(range)
    if op == '<':
        new_range[var][1] = min(val - 1, new_range[var][1])
    else:
        new_range[var][0] = max(val + 1, new_range[var][0])

    return new_range

def dfs(label: str, range: dict[str, list[int]]) -> int:
    if label == "A":
        ranges = [abs(max - min + 1) for min, max in range.values()]
        return reduce(mul, ranges, 1)
    elif label == "R":
        return 0

    total = 0
    for condition, result in workflows[label]:
        take_range = consider(range, condition, False)
        total += dfs(result, take_range)
        # now update what happens if don't take and continue processing the list
        range = consider(range, condition, True)

    return total

starting_range = {
    'x': [1, 4000],
    'm': [1, 4000],
    'a': [1, 4000],
    's': [1, 4000],
}

ans = dfs('in', starting_range)
print(ans)

