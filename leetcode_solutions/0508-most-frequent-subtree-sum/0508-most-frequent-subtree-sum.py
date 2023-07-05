# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        mapping = {}
        res = []
        def post_order(node):
            nonlocal mapping

            if not node:
                return 0

            left_sum = post_order(node.left)
            right_sum = post_order(node.right)
            total = node.val + left_sum + right_sum

            mapping[total] = mapping.get(total, 0) + 1

            return total
        
        post_order(root)

        # Capture max frequent of the map
        max_freq = 0
        for value in mapping.values():
            if value > max_freq:
                max_freq = value
                
        # Find the most frequent from the subtree sum.
        # If there is a tie, return all the values with the highest frequency in any order.
        for key, value in mapping.items():
            if value == max_freq:
                res.append(key)

        return res
        