Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> DFS (Depth-First Search) in Python
... DFS explores a graph by going as deep as possible along one path before backtracking. It uses a stack or recursion.
... 
... 1. DFS using recursion
... python
... def dfs(graph, node, visited):
...     if node not in visited:
...         print(node, end=" ")
...         visited.add(node)
... 
...         for neighbor in graph[node]:
...             dfs(graph, neighbor, visited)
... 
... 
... graph = {
...     'A': ['B', 'C'],
...     'B': ['D', 'E'],
...     'C': ['F'],
...     'D': [],
...     'E': ['F'],
...     'F': []
... }
... 
... visited = set()
... dfs(graph, 'A', visited)
... Output:
... 
... text
... A B D E F C
... 2. DFS using a stack (iterative)
... python
... def dfs(graph, start):
...     visited = set()
...     stack = [start]
... 
...     while stack:
...         node = stack.pop()
... 
...         if node not in visited:
...             print(node, end=" ")
...             visited.add(node)
... 
...             for neighbor in reversed(graph[node]):
...                 if neighbor not in visited:
...                     stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
Output:

text
A B D E F C
