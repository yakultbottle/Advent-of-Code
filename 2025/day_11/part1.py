input = open(0).read().strip().splitlines()

adj_list: dict[str, list[str]] = {}

for line in input:
    input, *output = line.split()
    adj_list[input[:-1]] = output

def num_ways(start: str) -> int:
    if start == "out":
        return 1

    count = 0
    for node in adj_list[start]:
        count += num_ways(node)
    return count

ans = num_ways("you")
print(ans)
