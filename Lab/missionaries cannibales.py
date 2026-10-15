from collections import deque

def solve():
    # State: (missionaries_left, cannibals_left, boat_position)
    # boat_position: 0 = left bank, 1 = right bank

    start = (3, 3, 0)
    goal = (0, 0, 1)

    moves = [
        (1, 0), (2, 0),  # Missionaries
        (0, 1), (0, 2),  # Cannibals
        (1, 1)           # One missionary and one cannibal
    ]

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            for step in path + [state]:
                print(step)
            print("Solution Found!")
            return

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            nm, nc, _ = new_state
            mr = 3 - nm
            cr = 3 - nc

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            if nm > 0 and nc > nm:
                continue

            if mr > 0 and cr > mr:
                continue

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    print("No solution found")

solve()
Sample Output
The program prints the sequence of states leading to the goal. Each state is represented as:

(M, C, B)

M = Missionaries on the left bank

C = Cannibals on the left bank

B = Boat position (0 = left, 1 = right)

The goal state is (0, 0, 1), meaning everyone has crossed to the right bank.
