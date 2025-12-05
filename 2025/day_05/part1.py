ranges, ingredients = [item.split("\n") for item in open(0).read().strip().split("\n\n")]
ingredients = list(map(int, ingredients))

seen = []
for r in ranges:
    start, end = map(int, r.split("-"))
    temp = range(start, end + 1)
    seen.append(temp)

count = 0
for ingredient in ingredients:
    for bound in seen:
        if ingredient in bound:
            count += 1
            break
print(count)
