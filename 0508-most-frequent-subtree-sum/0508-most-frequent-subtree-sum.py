# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def post_order(node):
            nonlocal mapping

            if not node:
                return 0

            left_sum = post_order(node.left)
            right_sum = post_order(node.right)
            total = node.val + left_sum + right_sum

            if total in mapping:
                mapping[total] += 1
            else:
                mapping[total] = 1

            return total
    
        mapping = {}
        res = []

        post_order(root)

        max_freq = 0
        for value in mapping.values():
            if value > max_freq:
                max_freq = value

        for key, value in mapping.items():
            if value == max_freq:
                res.append(key)

        return res
        