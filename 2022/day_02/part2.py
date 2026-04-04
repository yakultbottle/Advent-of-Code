input = open(0).read().strip()

score = 0
for line in input.split("\n"):
    opp, you = line.split()

    score += (ord(you) - ord("X")) * 3
    score += (ord(you) - ord("Y") + ord(opp) - ord("A")) % 3 + 1

    #   X Y Z
    # A 3 1 2
    # B 1 2 3
    # C 2 3 1

print(score)
