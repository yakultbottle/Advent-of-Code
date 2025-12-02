import sys

input = sys.stdin.read()

words = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

answer = 0
for line in input.strip().split("\n"):
    left = 0
    right = len(line) - 1

    while True:
        found_match = False
        if line[left] in nums:
            first = int(line[left])
            break

        word = ""
        for word in words:
            # print(line[left:left + len(word)], word, str(left))
            if line[left:left + len(word)] == word:
                found_match = True
                break

        if found_match:
            # print(word)
            first = int(words[line[left:left + len(word)]])
            break

        left += 1

    while True:
        found_match = False
        if line[right] in nums:
            second = int(line[right])
            break

        word = ""
        for word in words:
            # print(line[right - len(word) + 1:right + 1], word, str(right))
            if line[right - len(word) + 1:right + 1] == word:
                found_match = True
                break

        if found_match:
            # print(word)
            second = int(words[line[right - len(word) + 1:right + 1]])
            break

        right -= 1

    answer += first * 10 + second

print(answer)
