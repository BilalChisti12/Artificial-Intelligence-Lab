from collections import deque

goal = (1,2,3,4,5,6,7,8,0)

moves = {
    0:[1,3], 1:[0,2,4], 2:[1,5],
    3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
    6:[3,7], 7:[4,6,8], 8:[5,7]
}

def bfs(start):
    q = deque([(start, [])])
    seen = {start}

    while q:
        state, path = q.popleft()
        if state == goal:
            return path + [state]

        z = state.index(0)
        for m in moves[z]:
            s = list(state)
            s[z], s[m] = s[m], s[z]
            s = tuple(s)

            if s not in seen:
                seen.add(s)
                q.append((s, path + [state]))

def show(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

start = (1,2,3,4,0,6,7,5,8)
sol = bfs(start)

print("Moves:", len(sol) - 1, "\n")
for step in sol:
    show(step)