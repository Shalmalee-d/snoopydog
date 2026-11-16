
def water_jug_dfs(cap1, cap2, target):
    stack = [((0, 0), [(0, 0)])]
    visited = set()
    step = 0

    while stack:
        (a, b), path = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        step += 1
        print("Iteration", step, ":", (a, b))

        if a == target or b == target:
            print("\nGoal Reached!")
            return path

        states = [
            (cap1, b),
            (a, cap2),
            (0, b),
            (a, 0),
            (a - min(a, cap2-b), b + min(a, cap2-b)),
            (a + min(b, cap1-a), b - min(b, cap1-a))
        ]

        for s in states:
            if s not in visited:
                stack.append((s, path + [s]))

    return None


# Input
cap1 = int(input("Enter Jug 1 capacity: "))
cap2 = int(input("Enter Jug 2 capacity: "))
target = int(input("Enter target quantity: "))

path = water_jug_dfs(cap1, cap2, target)

# Display solution
if path:
    print("\nSolution Path:")
    for i, state in enumerate(path):
        print("Step", i, ":", state)
else:
    print("No solution exists.")
