from collections import deque

def adjacency_list(n, edges):
    adjacency = {}
    for i in range(1, n + 1):
        adjacency[i] = []

    for src, des in edges:
        adjacency[src].append(des)
        adjacency[des].append(src)
    return adjacency


def print_adj_list(adj_list):
    for key in sorted(adj_list.keys()):
        print(f"{key}: {adj_list[key]}")

# DFS recursively
def dfs_recursive(node, adj_list, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in adj_list[node]:
            dfs_recursive(neighbor, adj_list, visited)

# DFS iteratively
def dfs_iterative(start_node, adj_list):
    stack = [start_node]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# BFS
def bfs(start_node, adj_list):
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
n = 5  # Number of vertices
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (4, 5)]  # List of edges in the graph

adj_list = adjacency_list(n, edges)
print("Adjacency List:")
print_adj_list(adj_list)

print("\nDFS Recursive:")
visited = set()
dfs_recursive(5, adj_list, visited)

print("\nDFS Iterative:")
dfs_iterative(5, adj_list)

print("\nBFS:")
bfs(5, adj_list)

'''
   1 - 2 \
   |   |  5
   3 - 4 /
'''
