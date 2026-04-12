input = open(0).read().strip()

freq = [0] * 26

count = 0
for i, char in enumerate(input):
    assert char.islower()

    freq[ord(char) - ord("a")] += 1
    if i < 14:
        continue

    freq[ord(input[i - 14]) - ord("a")] -= 1

    for past_idx in range(i - 13, i):
        if freq[ord(input[past_idx]) - ord("a")] > 1:
            break
    else:
        count = i + 1
        break

print(count)
