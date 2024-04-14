# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, False)])  # Tuple: (node, is_left_child)
        res = 0
        
        while queue:
            node, is_left_child = queue.popleft()
            
            if is_left_child and not node.left and not node.right:  # Check if it's a left leaf
                res += node.val
                
            if node.left:
                queue.append((node.left, True))  # Marking the left child as a left child
            if node.right:
                queue.append((node.right, False))  # Right child is not a left child
            
        return res
        