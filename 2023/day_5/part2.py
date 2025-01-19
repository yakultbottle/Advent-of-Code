import sys

input = sys.stdin.read().strip()

seeds, _, maps = input.partition("\n\n")

seeds = seeds.partition(": ")[-1]
seeds = list(map(int, seeds.split()))

i = 0
temp = []
while i + 1 < len(seeds):
    temp.append((seeds[i], seeds[i] + seeds[i + 1]))
    i += 2
seeds = temp

for map in maps.split("\n\n"):
    _, _, lines = map.partition("\n")

    processed = []
    while seeds:
        seed_start, seed_end = seeds.pop()
        seed_range = range(seed_start, seed_end)

        transformed = False
        for line in lines.split("\n"):
            dest, src, len = [int(num) for num in line.split()]
            src_end = src + len
            src_range = range(src, src_end)

            new_seed = ()
            leftover_seeds = []

            if seed_start in src_range and seed_end in src_range:
                new_seed = (dest + (seed_start - src), dest + (seed_end - src))
                transformed = True
            elif seed_start in src_range:
                new_seed = (dest + (seed_start - src), dest + len)
                leftover_seeds.append((src_end, seed_end))
                transformed = True
            elif seed_end in src_range:
                if seed_end == src:
                    continue
                new_seed = (dest, dest + (seed_end - src))
                leftover_seeds.append((seed_start, src))
                transformed = True
            elif src in seed_range:
                new_seed = (dest, dest + len)
                leftover_seeds.append((seed_start, src))
                leftover_seeds.append((src_end, seed_end))
                transformed = True

            if transformed:
                if new_seed:
                    processed.append(new_seed)
                for leftover_seed in leftover_seeds:
                    seeds.append(leftover_seed)
                break

        if not transformed:
            processed.append((seed_start, seed_end))

    seeds = processed

answer = min(min(pair) for pair in seeds)
print(answer)

