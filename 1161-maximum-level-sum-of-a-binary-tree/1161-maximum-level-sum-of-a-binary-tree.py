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
            
            queue = collections.deque([root])
            levels_sum = []
            
            while queue:
                level_size = len(queue)
                total = 0
                
                for _ in range(level_size):
                    curr = queue.popleft()
                    total += curr.val

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

                    level_size -= 1

                levels_sum.append(total)

            maximal = levels_sum[0]
            max_index = 0
            for i in range(len(levels_sum)):
                curr = levels_sum[i]
                if curr > maximal:
                    max_index = i
                    maximal = curr

            return max_index + 1
        