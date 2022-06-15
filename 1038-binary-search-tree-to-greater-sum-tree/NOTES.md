​class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstToGst(root: TreeNode) -> TreeNode:
    if not root:
        return root

    curr = root
    total = 0
    stack = []
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.right

        curr = stack.pop()
        total += curr.val
        curr.val = total
        curr = curr.left

    return root



if __name__ == "__main__":
    # root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    '''
              4
           /     \
          1       6
         /  \    /  \
        0    2  5    7
              \       \
               3       8
    '''

    tree = TreeNode(4)
    tree.left = TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, TreeNode(3, None, None)))
    tree.right = TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, TreeNode(8, None, None)))
    print(bstToGst(tree))


