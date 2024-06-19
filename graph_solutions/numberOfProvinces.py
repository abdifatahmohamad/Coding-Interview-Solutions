from typing import List

n = 3
matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

# Create the adjacency list from the matrix
adjacency = {i: [] for i in range(1, n + 1)}
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            adjacency[i + 1].append(j + 1)

def print_adj_list():
    for key in adjacency.keys():
        print(f"{key}: {adjacency[key]}")

# Helper function to perform recursive DFS
def dfs(node, visited):
    visited.add(node)
    for neighbor in adjacency[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

def number_of_provinces(matrix: List[List[int]]) -> int:
    visited = set()
    provinces = 0

    # Perform DFS for each node
    for i in range(1, n + 1):
        if i not in visited:
            dfs(i, visited)
            provinces += 1
    
    return provinces

print("Adjacency List:")
print_adj_list()

print("\nDFS Recursive:")
visited = set()
dfs(1, visited)

print("\nNumber of Provinces:", number_of_provinces(matrix))  # Should print 2
