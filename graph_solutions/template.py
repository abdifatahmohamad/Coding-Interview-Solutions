from collections import defaultdict


n = 3  # Number of vertices
matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]  # Adjacency matrix


# adjacency = {}
# for i in range(1, n + 1):
#     adjacency[i] = []

adjacency = {i: [] for i in range(1, n + 1)}

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            adjacency[i + 1].append(j + 1)


def print_adj_list():
    for key in adjacency.keys():
        print(f"{key}: {adjacency[key]}")

# DFS recursively
def dfs(node, visited):
    print(node, end=" ")
    visited.add(node)
    for neighbor in adjacency[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
            
print("Adjacency List:")
print_adj_list()

print("\nDFS Recursive:")
visited = set()
dfs(1, visited)
