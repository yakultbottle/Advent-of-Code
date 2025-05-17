input = open(0).read().strip().split(",")

hashmap = [[] for _ in range(256)]

def hash_string(hash: str) -> int:
    box_num = 0
    for char in hash:
        box_num += ord(char)
        box_num *= 17
        box_num &= 0xFF
    return box_num

def print_hashmap(hashmap: list[list[tuple[str]]]):
    for i, box in enumerate(hashmap):
        if not box:
            continue
        print(f"Box {i}: {box}")
    
for step in input:
    is_add = (step[-1] != "-")

    if is_add:
        hash, num = step.split("=")
        box_num = hash_string(hash)
        for i in range(len(hashmap[box_num])):
            og_hash, og_num = hashmap[box_num][i]
            if hash == og_hash:
                hashmap[box_num][i] = (hash, num)
                break
        else:
            hashmap[box_num].append((hash, num))
    else:
        hash = step[:-1]
        box_num = hash_string(hash)
        for i in range(len(hashmap[box_num])):
            og_hash, og_num = hashmap[box_num][i]
            if hash == og_hash:
                hashmap[box_num].pop(i)
                break
    '''
    print_hashmap(hashmap)
    print()
    '''

'''
print("End")
print_hashmap(hashmap)
'''

ans = 0
for box_num, box in enumerate(hashmap):
    for slot, (lens, focal_length) in enumerate(box):
        ans += (box_num + 1) * (slot + 1) * int(focal_length)
print(ans)

