
# Python Program to Implement Uniform Cost Search (UCS)

import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': []
}

def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)

            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(
                        pq,
                        (cost + weight, neighbour,
                         path + [neighbour])
                    )

    return None

result = ucs('A', 'F')

print("Shortest Path:", result[1])
print("Total Cost:", result[0])
  
