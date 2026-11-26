
# Python Program to Implement Greedy Best First Search

import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

def greedy(start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = heapq.heappop(pq)

        if node == goal:
            print(node, end=" ")
            return

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(
                        pq, (heuristic[neighbour], neighbour)
                    )

print("Greedy Search:")
greedy('A', 'F')
