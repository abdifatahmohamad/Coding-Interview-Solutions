"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}
        return self.dfs(node, d)
    
    def dfs(self, node, d):
        if not node:
            return None

        if node in d:
            return d[node]

        clone = Node(node.val)
        d[node] = clone
        for nei in node.neighbors:
            clone.neighbors.append(self.dfs(nei, d))
        return clone
        
        
        
        
        
        
        
        
#         d = {}
#         copy = []
#         self.clone_helper(node, d, copy)
#         return copy

#     def clone_helper(self, node, d, copy) -> None:
#         if node in d:
#             return d[node]
#         d = {node}
#         copy = Node(node.val)
#         d[node] = copy
#         for nei in node.neighbors:
#             copy.neighbors.append(node, self.clone_helper(nei), copy)
#         return copy
        
        