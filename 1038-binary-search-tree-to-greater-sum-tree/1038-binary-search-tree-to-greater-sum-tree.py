# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        def dfs(root):
            nonlocal total
            if not root:
                return root

            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.right

                root = stack.pop()
                total += root.val
                root.val = total
                root = root.left
        dfs(root)
        return root
        