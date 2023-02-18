# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
            if not root:
                return []
            stack = []
            prev_val = float('-inf')
            min_diff = float('inf')
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left

                root = stack.pop()
                min_diff = min(min_diff, root.val - prev_val)
                prev_val = root.val
                root = root.right

            return min_diff
        