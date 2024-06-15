from collections import deque


class Solution:
    def __init__(self):
        self.adjacency = {}
        self.visited = set()

    def adjacency_list(self, n, edges):
        # Initialize the adjacency list
        self.adjacency = {}
        for i in range(1, n + 1):
            self.adjacency[i] = []
        
        # Populate the adjacency list based on the given edges
        for src, des in edges:
            self.adjacency[src].append(des)
            self.adjacency[des].append(src)

    def print_adjacency(self):
        for key in sorted(self.adjacency.keys()):
            print(f"{key}: {self.adjacency[key]}")

    # DFS recursively
    def dfs_recursive(self, node):
        if node not in self.visited:
            print(node, end=" ")
            self.visited.add(node)
            for neighbor in self.adjacency[node]:
                self.dfs_recursive(neighbor)

    # DFS iteratively
    def dfs_iterative(self, start_node):
        stack = [start_node]
        self.visited = set()

        while stack:
            node = stack.pop()
            if node not in self.visited:
                print(node, end=" ")
                self.visited.add(node)
                # Add neighbors to the stack
                for neighbor in self.adjacency[node]:
                    if neighbor not in self.visited:
                        stack.append(neighbor)
    # BFS
    def bfs(self, start_node):
        queue = deque([start_node])
        self.visited = set([start_node])

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.adjacency[node]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    queue.append(neighbor)

# Example usage:
n = 5  # Number of vertices
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (4, 5)]  # List of edges in the graph

solution = Solution()
solution.adjacency_list(n, edges)
print("Adjacency List:")
solution.print_adjacency()

print("\nDFS Recursive:")
solution.dfs_recursive(5)

print("\nDFS Iterative:")
solution.dfs_iterative(5)

print("\nBFS:")
solution.bfs(5)

'''
   1 - 2 \
   |   |  5
   3 - 4 /        
'''