import sys

targets = []
nums = []

def read_data():
    input_str = sys.stdin.readlines()

    for line in input_str:
        split = line.split(": ")
        targets.append(int(split[0]))
        temp = [int(num) for num in split[1].split(" ")]
        nums.append(temp)

    # return nothing, modify global arrays since im lazy
    return

def is_valid(total: int, target: int, row: list[int], idx: int) -> bool:
    if total == target and idx == len(row):
        return True
    if total > target or idx >= len(row):
        return False

    if is_valid(total + row[idx], target, row, idx + 1):
        return True
    if total != 0:
        if is_valid(total * row[idx], target, row, idx + 1):
            return True
        concat = int(str(total) + str(row[idx]))
        if is_valid(concat, target, row, idx + 1):
            return True
    return False

def main():
    answer = 0
    for i in range(len(targets)):
        if is_valid(0, targets[i], nums[i], 0):
            answer += targets[i]
    return answer

if __name__ == "__main__":
    read_data()
    output = main()
    print(output)
