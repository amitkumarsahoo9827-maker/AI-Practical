
# Python Program to Implement A* Search Algorithm

import heapq

graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(1, 0), (1, 2), (0, 1)],
    (1, 2): [(1, 1), (0, 2)]
}

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start, [start])]
    visited = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                new_cost = cost + 1
                new_f = new_cost + heuristic(neighbour, goal)

                heapq.heappush(
                    pq,
                    (new_f, new_cost, neighbour,
                     path + [neighbour])
                )

    return None

start = (0, 0)
goal = (1, 2)

result = astar(start, goal)

print("Path:", result[0])
print("Cost:", result[1])
