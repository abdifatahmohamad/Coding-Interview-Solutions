class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_similar(root1, root2) -> bool:
    ls1, ls2 = [], []

    def tree1(root1, ls1):
        if not root1:
            return root1

        if not root1.left and not root1.right:
            ls1.append(root1.val)

        return tree1(root1.left, ls1) or tree1(root1.right, ls1)

    def tree2(root2, ls2):
        if not root2:
            return root2

        if not root2.left and not root2.right:
            ls2.append(root2.val)

        return tree2(root2.left, ls2) or tree2(root2.right, ls2)

    tree1(root1, ls1)
    tree2(root2, ls2)

    return ls1 == ls2


# DFS iterative solution:
def leaf_similar_iter(root1, root2) -> bool:
    ls1, ls2 = [], []

    def tree1(root1):
        if not root1:
            return root1

        stack = [root1]
        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            if not node.left and not node.right:
                ls1.append(node.val)

    def tree2(root2):
        if not root2:
            return root2

        stack = [root2]
        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            if not node.left and not node.right:
                ls2.append(node.val)

    tree1(root1)
    tree2(root2)

    return ls1 == ls2


if __name__ == "__main__":
    '''
         1
       /   \
      2     3

    '''

    '''
          1
        /   \
       3     2 

     '''
    # Input: root1 = [1,2,3], root2 = [1,3,2]
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2, None, None)
    tree1.right = TreeNode(3, None, None)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(3, None, None)
    tree2.right = TreeNode(2, None, None)

    print(leaf_similar(tree1, tree2))
