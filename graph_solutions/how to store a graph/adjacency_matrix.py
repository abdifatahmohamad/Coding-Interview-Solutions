class Solution:
    def __init__(self):
        self.adj = []

    def adjacency_matrix(self, n, edges):
        # Initialize an (n+1) x (n+1) matrix with all zeros (considering 1-based indexing)
        self.adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        # Populate the adjacency matrix based on the given edges
        for edge in edges:
            u, v = edge
            self.adj[u][v] = 1
            self.adj[v][u] = 1

    def print_matrix(self):
        for row in self.adj:
            print(" ".join(map(str, row)))

# Example usage:
n = 5  # Number of vertices
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (4, 5)]  # List of edges in the graph

solution = Solution()
solution.adjacency_matrix(n, edges)
solution.print_matrix()

'''
   1 - 2 \
   |   |  5
   3 - 4 /        
'''