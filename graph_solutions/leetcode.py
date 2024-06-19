from collections import defaultdict
from typing import List

# If the graph bi-directional means graph in undirected

# n = 3
# edges = [[0,1],[1,2],[2,0]] # Edges isn't matrix
# source = 0
# destination = 2

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

# Create the adjacency list from the matrix
# adjacency = {i : [] for i in range(n)}
# for edge in edges:
#     u, v = edge
#     adjacency[u].append(v)
#     adjacency[u].append(u) # If the graph is undirected, add this line, remove if not

# Using defaultdict list collections
adjacency = defaultdict(list)
for src, des in edges:
    adjacency[src].append(des)
    adjacency[des].append(src) # If the graph is undirected, add this line, remove if not

def print_adjacency():
    for k, v in adjacency.items():
        print(f"{k}: {v}")

def dfs(node, visited):
    print(node, end="->")
    visited.add(node)
    for neighbor in adjacency[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # Using the global adjacency list created outside this function
    visited = set()
    dfs(source, visited)
    return destination in visited
    
print("Adjacency List:")
print_adjacency()

print("\nDFS Recursive:")
visited = set()
dfs(1, visited)

path_exists = validPath(n, edges, source, destination)
print(f"\nIs there a valid path from {source} to {destination}? {path_exists}")

