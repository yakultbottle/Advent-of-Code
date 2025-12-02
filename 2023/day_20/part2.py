from collections import defaultdict, deque
from functools import reduce

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


def step() -> bool:
    queue = deque([("broadcaster", "", False)])

    while queue:
        module_name, module_from, is_high = queue.popleft()
        new_low, new_high, queue = process_pulse(
            module_name, module_from, is_high, queue
        )

        if is_high and module_from in modules and "kc" in modules[module_from][2]:
            if module_from in cheat:
                continue
            cheat[module_from] = button_presses
            if len(cheat) >= 4:  # Suuuuuper hardcoded
                return True

    return False


button_presses = 0
cheat = defaultdict(int)

while True:
    button_presses += 1
    if step():
        break

cheat = list(cheat.values())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    if a > b:
        return (a * b) // gcd(a, b)
    return (a * b) // gcd(b, a)


ans = reduce(lcm, cheat)
print(ans)
