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
            res = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left

                root = stack.pop()
                res.append(root.val)
                root = root.right

            ans = [0 for _ in range(len(res)-1)]
            for i in range(len(res)-1):
                ans[i] = abs(res[i] - res[i + 1])
            return min(ans)
        