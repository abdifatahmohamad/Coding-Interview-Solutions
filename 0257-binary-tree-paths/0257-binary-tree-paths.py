# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []
        

        def dfs(root, path, paths):
            path += str(root.val)

            if not root.left and not root.right:
                paths.append(path)
            if root.left:
                dfs(root.left, path+"->", paths)
            if root.right:
                dfs(root.right, path+"->", paths)
        
        dfs(root, "", paths)
        return paths