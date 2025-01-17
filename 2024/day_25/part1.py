import sys

input = sys.stdin.read()

locks = set()
keys = set()

for item in input.split("\n\n"):
    is_lock = True if item[0] == "#" else False
    
    output = [0 for _ in range(5)]
    for i, line in enumerate(item.split("\n")):
        if i == 0 and is_lock:
            continue
        elif i == 6 and not is_lock:
            continue
        
        for j, character in enumerate(line.strip()):
            if character == "#":
                output[j] += 1

    if is_lock:
        locks.add(tuple(output))
    else:
        keys.add(tuple(output))

'''
print(locks)
print(keys)
'''

count = 0
for lock in locks:
    for key in keys:
        for pin, hole in zip(key, lock):
            if pin + hole > 5:
                break
        else:
            count += 1
print(count)
