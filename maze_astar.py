
# Python Program to Solve Maze Using A* Search Algorithm

import heapq

maze = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start, [start])]
    visited = set()

    while pq:
        f, cost, current, path = heapq.heappop(pq)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        r, c = current

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if (0 <= nr < len(maze) and
                0 <= nc < len(maze[0]) and
                maze[nr][nc] == 0):

                neighbour = (nr, nc)

                if neighbour not in visited:
                    new_cost = cost + 1
                    new_f = new_cost + heuristic(neighbour, goal)

                    heapq.heappush(
                        pq,
                        (new_f, new_cost, neighbour,
                         path + [neighbour])
                    )

    return None

path = astar(start, goal)

print("Maze Solution Path:")
print(path)
