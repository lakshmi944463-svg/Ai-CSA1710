from collections import deque

def water_jug():
    jug1 = 4
    jug2 = 3
    target = 2

    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == target:
            print("Goal Reached!")
            return

        states = [
            (jug1, y),  # Fill jug 1
            (x, jug2),  # Fill jug 2
            (0, y),     # Empty jug 1
            (x, 0),     # Empty jug 2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Solution not found")

water_jug()
Sample Output
text
0 0
4 0
0 3
4 3
1 3
3 1
1 0
3 3
4 2
Goal Reached!
