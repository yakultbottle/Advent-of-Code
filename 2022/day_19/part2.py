import re

input = open(0).read().strip().split("\n")

cost_idx = {
    "ore": 0,
    "clay": 1,
    "obsidian": 2,
    "geode": 3,
}

ans = 1
for line in input[:3]:
    id, rest = line.split(":")
    id = int(id.split()[-1])
    rest = rest[:-1].split(".")
    costs = [[0] * 4 for _ in range(4)]
    max_costs = [0] * 3

    for i, row in enumerate(costs):
        ores = re.findall(r'\d+ \w+', rest[i])

        for thing in ores:
            cost, ore = thing.split()
            costs[i][cost_idx[ore]] = int(cost)
            max_costs[cost_idx[ore]] = max(max_costs[cost_idx[ore]], int(cost))

    memo = {}
    def dfs(time: int, resources: tuple[int, int, int], robots: tuple[int, int, int, int]) -> int:
        if time == 0:
            return resources[-1]

        resources = tuple(
            min(amount, max(0, max_costs[i] * time - robots[i] * (time - 1)))
            for i, amount in enumerate(resources)
        )

        if (key := (time, resources, robots)) in memo:
            return memo[key]

        best = robots[-1] * time
        for idx in range(3, -1, -1):
            if idx < 3 and robots[idx] >= max_costs[idx]:
                continue

            cost = costs[idx][:3]

            waiting = 0
            impossible = False
            for i, required in enumerate(cost):
                shortage = required - resources[i]

                if shortage <= 0:
                    continue
                if robots[i] == 0:
                    impossible = True
                    break

                waiting = max(waiting, (shortage + robots[i] - 1) // robots[i])

            if impossible:
                continue

            elapsed = waiting + 1
            if elapsed >= time:
                continue

            next_resources = tuple(
                resources[i] + robots[i] * elapsed - cost[i]
                for i in range(3)
            )

            next_robots = list(robots)
            next_robots[idx] += 1
            next_robots = tuple(next_robots)

            remaining = time - elapsed

            upper_bound = (
                robots[3] * elapsed
                + next_robots[3] * remaining
                + remaining * (remaining - 1) // 2
            )

            if best >= upper_bound:
                continue

            best = max(best, robots[-1] * elapsed + dfs(remaining, next_resources, next_robots))

        memo[key] = best
        return best

    ans *= dfs(32, (0, 0, 0), (1, 0, 0, 0))

print(ans)
