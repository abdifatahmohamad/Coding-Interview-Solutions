from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    # Iterative solution
    def find_paths(self, root: TreeNode) -> None:
        path_paths_helper(root, "")

    def sum_path(self, root: TreeNode) -> List:
        lst = []
        sum_path_helper(root, lst, 0)
        return lst


def path_paths_helper(root, cur_val):
    # Base case:
    if not root:
        return

    cur_val += str(root.val) + " -> "
    # cur_val += (" —> " if cur_val else "\n") + str(root.val)
    if root.left is None and root.right is None:
        print(cur_val, "None")

    path_paths_helper(root.left, cur_val)
    path_paths_helper(root.right, cur_val)


def sum_path_helper(root, lst, curSum) -> List:
    if not root:
        return lst

    curSum += root.val
    if not root.left and not root.right:
        lst.append(curSum)

    sum_path_helper(root.left, lst, curSum)
    sum_path_helper(root.right, lst, curSum)


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
solution.find_paths(tree)
print(solution.sum_path(tree))
