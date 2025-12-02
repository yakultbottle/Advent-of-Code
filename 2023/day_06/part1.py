import sys

input = sys.stdin.read().strip()
time, distance = input.split("\n")

time = time.split(":")[-1].strip()
distance = distance.split(":")[-1].strip()

time = list(map(int, time.split()))
distance = list(map(int, distance.split()))

answer = 1
for idx in range(len(time)):
    count = 0

    for charge in range(time[idx]):
        time_remaining = time[idx] - charge
        distance_covered = time_remaining * charge

        if distance_covered > distance[idx]:
            count += 1

    answer *= count

print(answer)
