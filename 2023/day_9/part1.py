input = open(0).read().strip().split("\n")
input = [[int(num) for num in line.split()] for line in input]

def next_num(line: list[int]) -> int:
    differences = []
    all_zero = True

    i = 0
    while i + 1 < len(line):
        diff = line[i + 1] - line[i]
        if diff != 0:
            all_zero = False
        differences.append(diff)
        i += 1

    if all_zero:
        return line[-1]

    return line[-1] + next_num(differences)

answer = 0
for line in input:
    answer += next_num(line)

print(answer)
