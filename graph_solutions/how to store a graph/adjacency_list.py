class Solution:
    def __init__(self):
        self.adj_list = {}

    def adjacency_list(self, n, edges):
        # Initialize the adjacency list
        self.adj_list = {i: [] for i in range(1, n + 1)}
        
        # Populate the adjacency list based on the given edges
        for edge in edges:
            u, v = edge
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def print_adj_list(self):
        for key in sorted(self.adj_list.keys()):
            print(f"{key}: {self.adj_list[key]}")

# Example usage:
n = 5  # Number of vertices
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (4, 5)]  # List of edges in the graph

solution = Solution()
solution.adjacency_list(n, edges)
solution.print_adj_list()

'''
   1 - 2 \
   |   |  5
   3 - 4 /        
'''