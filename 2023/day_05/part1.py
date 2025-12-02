import sys

input = sys.stdin.read().strip()

seeds, _, maps = input.partition("\n\n")

seeds = seeds.partition(": ")[-1]
seeds = list(map(int, seeds.split()))

for map in maps.split("\n\n"):
    _, _, lines = map.partition("\n")

    changed = set()
    for line in lines.split("\n"):
        dest, src, len = [int(num) for num in line.split()]

        for i, seed in enumerate(seeds):
            if i in changed:
                continue
            if seed not in range(src, src + len):
                continue
            
            changed.add(i)
            seeds[i] = dest + (seed - src)

# print(seeds)
print(min(seeds))
