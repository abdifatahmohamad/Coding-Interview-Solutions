# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        curr = root
        total = 0
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            total += curr.val
            curr.val = total
            curr = curr.left

        return root
        