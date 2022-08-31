# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        
        def inorder(node) -> None:
            if not node:
                return
            
            stack = []
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                    
                node = stack.pop()
                lst.append(node.val)
                node = node.right
        
        def build_tree(left, right):
            if left > right:
                return None
            
            mid = left + right >> 1
            node = TreeNode(lst[mid])
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            return node
        
        inorder(root)
        return build_tree(0, len(lst)-1)
                
        