# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1) == self.dfs(root2)
    
    @staticmethod
    def dfs(root):
        if not root:
            return
        
        stack, leaves = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if not root.left and not root.right:
                leaves.append(root.val)
            root = root.right
            
        return leaves

    
  
    
    
    
    