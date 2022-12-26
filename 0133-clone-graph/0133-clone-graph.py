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
        
        def dfs(node):
            if not node:
                return None
            
            if node in d:
                return d[node]
            
            clone = Node(node.val)
            d[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        
        return dfs(node)
        
        
        
        
        
        
        
        
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
        
        