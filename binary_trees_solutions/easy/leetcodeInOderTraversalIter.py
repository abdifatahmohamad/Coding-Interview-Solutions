import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


# In order traversal
def inorder_traversal(root):
    if not root:
        return
    res, stack = [], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res


if __name__ == "__main__":
    '''
            3
           /  \
          9    20
              /  \
             15   7 
    '''

    tree = TreeNode(3)
    tree.left = TreeNode(9, None, None)
    tree.right = TreeNode(20, TreeNode(15, None, None),
                          TreeNode(7, None, None))
    print(inorder_traversal(tree))  # [9, 3, 15, 20, 7]
