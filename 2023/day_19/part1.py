from collections import defaultdict

workflows_str, parts = open(0).read().strip().split("\n\n")

def parse_rules(string: str) -> list[tuple[str, str]]:
    rules_str = string.split(",")

    rules = []
    for rule_str in rules_str:
        if ':' not in rule_str:
            condition = 'True'
            result = rule_str
        else:
            condition, result = rule_str.split(":")
        rules.append((condition, result))
    return rules

workflows = defaultdict(list)
for workflow in workflows_str.split("\n"):
    label, rules = workflow[:-1].split("{")
    workflows[label] = parse_rules(rules)

parts = [[int(x[2:]) for x in part[1:-1].split(",")] for part in parts.split("\n")]

ans = 0
for x, m, a, s in parts:
    label = 'in'
    while label not in ("A", "R"):
        for condition, result in workflows[label]:
            if eval(condition):
                label = result
                break

    if label == "A":
        ans += x + m + a + s
print(ans)

