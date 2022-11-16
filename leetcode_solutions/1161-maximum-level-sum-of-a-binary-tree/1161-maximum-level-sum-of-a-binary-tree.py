# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = depth = 0
        comm = float("-Inf")
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            total = 0
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            if total > comm:
                comm = total
                res = depth
        return  res
            
        
        
        