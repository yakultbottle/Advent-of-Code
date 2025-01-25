input = open(0).read().strip()

def perms(springs: str, groups: tuple) -> int:
    if springs == "":
        return 1 if groups == () else 0

    if groups == ():
        return 0 if "#" in springs else 1
    
    result = 0

    if springs[0] in ".?": # if first spring operational
        result += perms(springs[1:], groups)
    if springs[0] in "#?": # if first spring faulty
        if (groups[0] <= len(springs) and "." not in springs[:groups[0]]
                and (groups[0] == len(springs) or springs[groups[0]] != "#")):
            result += perms(springs[groups[0] + 1:], groups[1:])

    return result

total = 0
for line in input.split("\n"):
    springs, groups = line.split()
    groups = tuple(map(int, groups.split(",")))

    permutations = perms(springs, groups)
    
    total += permutations

print(total)
