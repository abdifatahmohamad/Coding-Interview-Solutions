# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lst = []      
        if not root:
            return lst

        stack = [root]
        while stack:
            node = stack.pop()
            lst.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        mapping = {}
        for i in range(len(lst)):
            curr = lst[i]
            complement = k - curr
            if complement in mapping:
                return True
            else:
                mapping[curr] = i
        return False

        
                
        