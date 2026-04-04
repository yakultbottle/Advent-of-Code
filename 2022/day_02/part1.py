input = open(0).read().strip()

score = 0
for line in input.split("\n"):
    opp, you = line.split()

    score += ord(you) - ord("X") + 1
    score += (ord(you) - ord(opp) - ord("X") + ord("A") + 1) % 3 * 3

    #   X Y Z
    # A 1 2 0
    # B 0 1 2
    # C 2 0 1

print(score)
