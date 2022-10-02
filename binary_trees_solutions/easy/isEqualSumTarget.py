class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    # Iterative solution
    def isEqualSumTarget(self, root: TreeNode, target: int) -> bool:
        if not root and target == 0:
            return False

        stack = [(root, target)]
        while stack:
            curr, target = stack.pop()
            if not curr and target != 0:
                return False

            target -= curr.val
            if curr.left is None and curr.right is None and target == 0:
                return True

            if curr.left:
                stack.append((curr.left, target))
            if curr.right:
                stack.append((curr.right, target))
        return False

    # Recursive solution
    def isEqualSumTarget1(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False

        target -= root.val
        if root.left is None and root.right is None and target == 0:
            return True

        return self.isEqualSumTarget1(root.left, target) or \
            self.isEqualSumTarget1(root.right, target)

    # Another recursive solution using dfs function and boolean flag "targetFound"
    def isEqualSumTarget2(self, root: TreeNode, target: int) -> bool:
        targetFound = False

        def dfs(node, target):
            nonlocal targetFound
            if not node:
                return False

            target -= node.val
            if not node.left and not node.right and target == 0:
                targetFound = True

            dfs(node.left, target)
            dfs(node.right, target)

        dfs(root, target)
        return targetFound


"""

       10
      /  \
     8    2
    / \   /
   3   5 2

target = 23

"""

tree = TreeNode(10)
tree.left = TreeNode(8)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(2)

solution = Solution()
print(solution.isEqualSumTarget(tree, 23))
print(solution.isEqualSumTarget(tree, 77))

print(solution.isEqualSumTarget1(tree, 23))
print(solution.isEqualSumTarget1(tree, 5))

print(solution.isEqualSumTarget2(tree, 23))
print(solution.isEqualSumTarget2(tree, 101))
