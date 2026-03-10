from collections import deque

# State: (monkey_pos, box_pos, on_box, has_banana)
# Positions: "left", "middle", "right"
start = ("left", "middle", False, False)
goal = lambda s: s[3]

positions = ["left", "middle", "right"]

def next_states(state):
    m, b, on_box, has = state
    result = []

    # Walk
    if not on_box:
        for p in positions:
            if p != m:
                result.append(((p, b, False, False), f"Walk to {p}"))

    # Push box
    if m == b and not on_box:
        for p in positions:
            if p != m:
                result.append(((p, p, False, False), f"Push box to {p}"))

    # Climb box
    if m == b and not on_box:
        result.append(((m, b, True, False), "Climb box"))

    # Grab banana (banana is in middle)
    if on_box and m == "middle":
        result.append(((m, b, True, True), "Grab banana"))

    return result

def bfs():
    q = deque([(start, [])])
    seen = {start}

    while q:
        state, path = q.popleft()
        if goal(state):
            return path

        for nxt, action in next_states(state):
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, path + [action]))

solution = bfs()

for i, step in enumerate(solution, 1):
    print(f"{i}. {step}")