import sys
# from functools import cache

# sys.setrecursionlimit(5000)
modulo = 0xFFFFFF # 2^24

'''
memo = {}
# @cache
def find_secret(secret: int, depth: int):
    if (secret, depth) in memo:
        return memo[(secret, depth)]
    if depth == 0:
        return secret

    next_secret = secret
    next_secret ^= (next_secret << 6) # * 64
    next_secret &= modulo
    next_secret ^= (next_secret >> 5) # / 32
    next_secret &= modulo
    next_secret ^= (next_secret << 11) # * 2048
    next_secret &= modulo

    memo[(secret, depth)] = find_secret(next_secret, depth - 1)
    return memo[(secret, depth)]
    # return find_secret(next_secret, depth - 1)
'''

def find_secret(secret: int, depth: int) -> int:
    next_secret = secret
    for _ in range(depth):
        next_secret ^= (next_secret << 6) # * 64
        next_secret &= modulo
        next_secret ^= (next_secret >> 5) # / 32
        next_secret &= modulo
        next_secret ^= (next_secret << 11) # * 2048
        next_secret &= modulo
    return next_secret

input = list(map(int, sys.stdin.read().splitlines()))
 
depth = 2000
count= 0
for secret in input:
    count += find_secret(secret, depth)

print(count)
