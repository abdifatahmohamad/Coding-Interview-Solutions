class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]

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
