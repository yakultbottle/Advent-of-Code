from collections import defaultdict, deque

input = open(0).read().strip().split("\n")

module_type = None
modules: defaultdict[str, tuple[str, dict[str, bool], list[str], list[str]]] = (
    defaultdict(tuple)
)
for module in input:
    module_name, _, *next_modules = module.split(" ")
    next_modules = [name.rstrip(",") for name in next_modules]

    if module_name != "broadcaster":
        module_type, module_name = module_name[0], module_name[1:]
    else:
        module_type = ""

    # empty list is prev_modules, update in another loop since idk how do nicely
    modules[module_name] = (module_type, {}, next_modules, [])

for module_name, (
    module_type,
    module_state,
    next_modules,
    prev_modules,
) in modules.items():
    if not module_type:
        continue

    for module in next_modules:
        if module not in modules:
            continue
        modules[module][-1].append(module_name)

for module_name, (
    module_type,
    module_state,
    next_modules,
    prev_modules,
) in modules.items():
    if not module_type:
        continue
    elif module_type == "%":
        modules[module_name][1][""] = False
    else:
        for p in prev_modules:
            modules[module_name][1][p] = False


def hash_state(
    curr: defaultdict[str, tuple[str, dict[str, bool], list[str], list[str]]],
):
    return tuple(
        (module_name, tuple(sorted(module_state.items())))
        for module_name, (
            _,
            module_state,
            _,
            _,
        ) in curr.items()
    )


def send_pulse(
    next_modules: list[str],
    curr_model: str,
    send_high: bool,
    queue: deque[tuple[str, str, bool]],
) -> tuple[int, int, deque[tuple[str, str, bool]]]:
    low_count, high_count = 0, 0
    for next_m in next_modules:
        queue.append((next_m, curr_model, send_high))
        low_count += 0 if send_high else 1
        high_count += 1 if send_high else 0

    return (low_count, high_count, queue)


def process_pulse(
    module_name: str,
    module_from: str,
    receive_high: bool,
    queue: deque[tuple[str, str, bool]],
) -> tuple[int, int, deque[tuple[str, str, bool]]]:
    count = (0, 0, queue)
    if module_name not in modules:
        return count

    module_type, module_state, next_modules, prev_modules = modules[module_name]

    if module_name == "broadcaster":
        count = send_pulse(next_modules, module_name, receive_high, queue)
    elif module_type == "%":
        if not receive_high:
            module_state[""] = not module_state[""]
            count = send_pulse(next_modules, module_name, module_state[""], queue)
    elif module_type == "&":
        module_state[module_from] = receive_high
        pulse = not all(module_state.values())
        count = send_pulse(next_modules, module_name, pulse, queue)
    else:
        "scream"

    modules[module_name] = (module_type, module_state, next_modules, prev_modules)

    # print(module_name, module_state, count)
    return count


def step() -> tuple[int, int]:
    low_pulse, high_pulse = 1, 0
    queue = deque([("broadcaster", "", False)])

    while queue:
        module_name, module_from, is_high = queue.popleft()
        new_low, new_high, queue = process_pulse(
            module_name, module_from, is_high, queue
        )
        low_pulse += new_low
        high_pulse += new_high

    return (low_pulse, high_pulse)


# print(modules)
# print()
# low, high = step()
# print(low, high)

memo = {}
# memo[hash_state(modules)] = (0, 0, 0)

total_low, total_high = 0, 0
iter = 0
cycle_already_found = False
while iter < 1000:
    iter += 1

    low, high = step()
    # hash = hash_state(modules)
    total_low += low
    total_high += high

    # rip, this optimisation is slower for even up to 100k cycles. smth about the memory

    # if cycle_already_found or hash not in memo:
    #     memo[hash] = (iter, total_low, total_high)
    #     continue

    # cycle_already_found = True
    # cycle_start, cumul_low, cumul_high = memo[hash]
    # cycle_length = iter - cycle_start
    # cycle_low, cycle_high = total_low - cumul_low, total_high - cumul_high
    # num_full_cycles_left = (1000 - iter) % cycle_length
    # iter += num_full_cycles_left * cycle_length
    # total_low += num_full_cycles_left * cycle_low
    # total_high += num_full_cycles_left * cycle_high
    # print(cycle_length)

print(total_low, total_high)
ans = total_low * total_high
print(ans)
