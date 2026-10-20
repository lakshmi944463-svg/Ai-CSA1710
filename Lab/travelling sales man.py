The Travelling Salesman Problem (TSP) is an optimization problem in which a salesman must visit every city exactly once, return to the starting city, and minimize the total travel distance.

Here is a Python implementation using Dynamic Programming with Bitmasking, which finds the optimal tour.

Python code

python

def tsp(graph, n):
    INF = float('inf')

    # dp[mask][i] = minimum cost to visit cities in mask
    # and finish at city i
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    # Start from city 0
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue

            # Try visiting an unvisited city v
            for v in range(n):
                if mask & (1 << v) == 0:
                    new_mask = mask | (1 << v)
                    new_cost = dp[mask][u] + graph[u][v]

                    if new_cost < dp[new_mask][v]:
                        dp[new_mask][v] = new_cost
                        parent[new_mask][v] = u

    # Return to the starting city
    full_mask = (1 << n) - 1
    min_cost = INF
    last_city = -1

    for i in range(1, n):
        cost = dp[full_mask][i] + graph[i][0]
        if cost < min_cost:
            min_cost = cost
            last_city = i

    # Reconstruct the optimal path
    path = []
    mask = full_mask
    city = last_city

    while city != -1:
        path.append(city)
        prev = parent[mask][city]
        mask ^= (1 << city)
        city = prev

    path.reverse()
    path.append(0)

    return min_cost, path


# Example distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

cost, path = tsp(graph, n)

print("Minimum cost:", cost)
print("Optimal path:", " -> ".join(str(city) for city in path))
Output

text
Minimum cost: 80
Optimal path: 0 -> 2 -> 3 -> 1 -> 0
How it works
Initialize: Start at city 0 with a cost of 0.

Bitmasking: Represent visited cities using bits in an integer. For example, 0101 means cities 0 and 2 have been visited.

Dynamic programming: Calculate the minimum cost of reaching each city for every possible set of visited cities.

Return to start: Add the cost of returning to city 0 and choose the minimum.

Reconstruct the path: Use the parent table to recover the optimal tour.

Complexity analysis
Time complexity: 
O
(
n
2
2
n
)
O(n 
2
 2 
n
 )

Space complexity: 
O
(
n
2
n
)
O(n2 
n
 )

Here, 
n
n is the number of cities.

