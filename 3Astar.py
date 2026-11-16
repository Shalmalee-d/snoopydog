
import heapq

# Manhattan Distance
def heuristic(state, goal):
    d = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            d += abs(i//3 - j//3) + abs(i%3 - j%3)
    return d

# Generate valid moves
def neighbors(state):
    result = []
    zero = state.index(0)

    for move, direction in [(-3, "Up"), (3, "Down"),
                            (-1, "Left"), (1, "Right")]:
        new = zero + move

        if 0 <= new < 9 and abs(zero//3 - new//3) + abs(zero%3 - new%3) == 1:
            s = list(state)
            s[zero], s[new] = s[new], s[zero]
            result.append((tuple(s), direction))

    return result

# A* Search
def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start)]
    best = {start: 0}
    parent = {start: (None, "Start")}
    explored = 0

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != best[state]:
            continue

        explored += 1

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state][0]

            path.reverse()
            print("\nSolution found!")
            print("Minimum moves:", len(path) - 1)
            print("States explored:", explored)

            for step, s in enumerate(path):
                h = heuristic(s, goal)
                print(f"\nStep {step}: g={step}, h={h}, f={step+h}")
                print("Move:", "Start" if step == 0 else parent[s][1])

                for i in range(0, 9, 3):
                    print(*s[i:i+3])
            return

        for nxt, direction in neighbors(state):
            new_g = g + 1

            if new_g < best.get(nxt, float('inf')):
                best[nxt] = new_g
                parent[nxt] = (state, direction)
                heapq.heappush(pq, (new_g + heuristic(nxt, goal),
                                    new_g, nxt))

    print("No solution found!")

# Input
start = tuple(map(int, input("Enter initial state (0 = blank): ").split()))
goal = tuple(map(int, input("Enter goal state (0 = blank): ").split()))

astar(start, goal)
