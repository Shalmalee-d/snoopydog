
import random

# Calculate total route distance
def distance(route, graph):
    total = 0
    for i in range(len(route)):
        total += graph[route[i]][route[(i+1) % len(route)]]
    return total

# Generate neighbouring routes
def neighbors(route):
    result = set()
    for i in range(1, len(route)):
        for j in range(i+1, len(route)):
            r = list(route)
            r[i], r[j] = r[j], r[i]
            result.add(tuple(r))
    return result

# Local Beam Search
def beam_search(graph, k):
    n = len(graph)

    beam = set()
    while len(beam) < min(k, 10):
        route = tuple([0] + random.sample(range(1, n), n-1))
        beam.add(route)

    beam = sorted(beam)
    best = min(beam, key=lambda r: distance(r, graph))

    print("\nInitial Routes:")
    for r in beam:
        print(r, "Distance:", distance(r, graph))

    for step in range(10):
        candidates = set(beam)

        for r in beam:
            candidates.update(neighbors(r))

        new_beam = sorted(candidates, key=lambda r: distance(r, graph))[:k]

        print("\nIteration", step+1)
        for r in new_beam:
            print(r, "Distance:", distance(r, graph))

        if distance(new_beam[0], graph) < distance(best, graph):
            best = new_beam[0]

        print("Best Route:", best)
        print("Best Distance:", distance(best, graph))

        if new_beam == beam:
            print("Search stopped.")
            break

        beam = new_beam

    return best

# Input
n = int(input("Enter number of cities: "))
cities = input("Enter city names: ").split()

graph = []
print("Enter distance matrix:")

for i in range(n):
    graph.append(list(map(int, input().split())))

k = int(input("Enter beam width (K): "))

random.seed(1)
best = beam_search(graph, k)

# Final result
names = [cities[i] for i in best]
names.append(names[0])

print("\nFinal Result")
print("Best Route:", " -> ".join(names))
print("Total Distance:", distance(best, graph))
