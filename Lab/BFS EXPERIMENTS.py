BFS (Breadth-First Search) in Python
BFS is a graph traversal algorithm that explores nodes level by level. It uses a queue (FIFO) to keep track of which node to visit next.

Python BFS code
python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
Output:

text
A B C D E F
How BFS works
A

B

C

D, E

F

Visit the starting node first, then its neighbors, followed by the next level.
