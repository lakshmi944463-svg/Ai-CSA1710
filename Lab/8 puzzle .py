import heapq

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)  # 0 represents the blank tile


# Calculate Manhattan distance
def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_index = tile - 1
            distance += abs(i // 3 - goal_index // 3)
            distance += abs(i % 3 - goal_index % 3)

    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = blank // 3, blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)

            new_state[blank], new_state[new_pos] = (
                new_state[new_pos], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* search algorithm
def solve(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))

    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == GOAL:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        if g != cost[current]:
            continue

        for neighbor in get_neighbors(current):
            new_cost = g + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                priority = new_cost + heuristic(neighbor)
                heapq.heappush(
                    pq, (priority, new_cost, neighbor)
                )

    return None


# Print puzzle state
def display(state):
    for i in range(0, 9, 3):
        print(*[x if x != 0 else "_" for x in state[i:i + 3]])
    print()


# Main program
start = tuple(map(int, input(
    "Enter 9 numbers (0 for blank): "
).split()))

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter each number from 0 to 8 once.")
else:
    path = solve(start)

    if path:
        print("Solution found in", len(path) - 1, "moves:\n")

        for step, state in enumerate(path):
            print("Step", step)
            display(state)
    else:
        print("No solution exists.")
Sample input
text
1 2 3 4 0 6 7 5 8
Here, 0 represents the blank space.

Sample output
text
Solution found in 2 moves:

Step 0
1 2 3
4 _ 6
7 5 8

Step 1
1 2 3
4 5 6
7 _ 8

Step 2
1 2 3
4 5 6
7 8 _