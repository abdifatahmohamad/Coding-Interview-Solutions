class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def inorder_traversal(self, root):
        # Base case:
        if not root:
            return

        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)


def build_tree():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    tree.left.right.right = TreeNode(8)
    tree.right.right.right = TreeNode(9)

    tree.inorder_traversal(tree)


#                1
#              /   \
#             2     3
#            /  \  /  \
#           4    5 6   7
#                 \     \
#                  8     9

if __name__ == "__main__":
    build_tree()
