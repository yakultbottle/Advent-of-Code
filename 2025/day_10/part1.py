input = open(0).read().strip().split("\n")

ans = 0
for row in input:
    first, *second, _ = row.split()
    end_state = [char == "#" for char in first[1:-1]]
    switches = [list(map(int, switch[1:-1].split(","))) for switch in second]

    curr_state = [False for _ in range(len(end_state))]
    n = len(switches)

    def knapsack(idx: int, count: int) -> int:
        if curr_state == end_state:
            return count
        if idx >= n:
            return float('inf')

        minSoFar = float('inf')
        for i in range(idx, n):
            for switch in switches[i]:
                curr_state[switch] = not curr_state[switch]
            take = knapsack(i + 1, count + 1)
            for switch in switches[i]:
                curr_state[switch] = not curr_state[switch]
            dontTake = knapsack(i + 1, count)
            minSoFar = min(minSoFar, take, dontTake)
        return minSoFar

    ans += knapsack(0, 0)

print(ans)
