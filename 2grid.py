from collections import deque

print("Enter the 4 x 4 grid")
print("Use S for Start, G for Goal, 0 for Free cell and X for Obstacle")

grid = []

for i in range(4):
    row = input(f"Enter row {i + 1}: ").strip()

    # Accept both "S 0 X X" and "S0XX"
    if " " in row:
        row = row.split()
    else:
        row = list(row)

    if len(row) != 4:
        print("Each row must contain exactly 4 cells.")
        exit()

    grid.append(row)

# Find Start and Goal positions
start = None
goal = None

for i in range(4):
    for j in range(4):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# Check whether Start and Goal exist
if start is None or goal is None:
    print("Error: Grid must contain one S and one G.")
    exit()

# Queue stores current position and path
queue = deque([(start, [start])])

# Internal state of the agent
visited = set()
visited.add(start)

# Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print("\nGrid Navigation Begins\n")

final_path = None

while queue:

    current, path = queue.popleft()

    print("Current Position:", current)
    print("Visited:", visited)

    # Goal test
    if current == goal:
        final_path = path 
        print("\nGoal Reached!")
        break

    # Explore neighbours
    for dr, dc in directions:

        nr = current[0] + dr
        nc = current[1] + dc

        # Check grid boundary
        if 0 <= nr < 4 and 0 <= nc < 4:

            # Skip obstacles
            if grid[nr][nc] == 'X':
                continue

            # Skip visited cells
            if (nr, nc) in visited:
                continue

            # Update internal state
            visited.add((nr, nc))

            # Add neighbour to queue
            queue.append(((nr, nc), path + [(nr, nc)]))

print("\n====================")

if final_path:
    print("Path Found:")
    print(final_path)
else:
    print("No path exists.")
