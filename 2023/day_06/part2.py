import sys

input = sys.stdin.read().strip()
time, distance = input.split("\n")

time = time.split(":")[-1].strip()
distance = distance.split(":")[-1].strip()

time = int("".join(time.split()))
distance = int("".join(distance.split()))

start = 0
end = time // 2

minSoFar = -1
while start <= end:
    mid = (start + end) // 2

    time_remaining = time - mid
    distance_covered = time_remaining * mid

    if distance_covered > distance:
        minSoFar = mid
        end = mid - 1
    else:
        start = mid + 1

start = time // 2 + 1
end = time

maxSoFar = -1
while start <= end:
    mid = (start + end) // 2

    time_remaining = time - mid
    distance_covered = time_remaining * mid

    if distance_covered > distance:
        maxSoFar = mid
        start = mid + 1
    else:
        end = mid - 1

num_ways = maxSoFar - minSoFar + 1
print(num_ways)
