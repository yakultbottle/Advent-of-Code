from collections import defaultdict, deque

input = open(0).read().strip().split("\n")
unique = set()

adj_list = defaultdict(list)
for line in input:
    src, *dests = line.split()
    src = src[:-1]
    unique.add(src)

    for dest in dests:
        unique.add(dest)
        adj_list[src].append(dest)
        adj_list[dest].append(src)

n = len(input)
num_nodes = len(unique)


def maxFlow(src: str, dest: str):
    used_edges = set()
    max_flow = 0

    def bfs() -> tuple[bool, int]:
        visited = set()
        visited.add(src)
        parent = {}
        found_dest = False

        frontier = deque()
        frontier.appendleft(src)
        while frontier:
            curr = frontier.pop()

            if curr == dest:
                found_dest = True
                while curr != src:
                    prev = parent[curr]

                    if (curr, prev) in used_edges:
                        used_edges.remove((curr, prev))
                    else:
                        used_edges.add((prev, curr))

                    curr = prev
                break

            for node in adj_list[curr]:
                if node in visited:
                    continue
                if (curr, node) in used_edges:
                    continue

                frontier.appendleft(node)
                visited.add(node)
                parent[node] = curr

        return found_dest, len(visited)

    cluster_size = -1
    while max_flow <= 3:
        found_dest, cluster_size = bfs()
        if not found_dest:
            break
        max_flow += 1

    return max_flow == 3, cluster_size


nodes = list(unique)
src = nodes[0]
ans = -1
for dest in nodes:
    if dest == src:
        continue

    done, cluster_size = maxFlow(src, dest)

    if done:
        ans = cluster_size * (num_nodes - cluster_size)
        break


print(ans)
