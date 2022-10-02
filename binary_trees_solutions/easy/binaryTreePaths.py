from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    # Find BT paths recursively
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        self.dfs(root, "", paths)
        return paths

    def dfs(self, root, path, paths):
        path += str(root.val)

        if not root.left and not root.right:
            paths.append(path)
        if root.left:
            self.dfs(root.left, path+"->", paths)
        if root.right:
            self.dfs(root.right, path+"->", paths)

    # Find BT paths iteratively
    def binaryTreePathsStack(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                paths.append(path)

            if node.left:
                stack.append((node.left, path+"->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path+"->" + str(node.right.val)))
        return paths


"""
           5
          /  \
         4    8
        / \   / \
      11   5 13  4
     /  \         \
    7    2         1


"""

tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(11)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(13)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)

solution = Solution()
print(solution.binaryTreePaths(tree))
print(solution.binaryTreePathsStack(tree))
