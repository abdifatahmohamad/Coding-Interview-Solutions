import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def min_depth(root) -> int:
    minimum_depth = 0

    def bfs(root):
        nonlocal minimum_depth
        if not root:
            return minimum_depth

        queue = collections.deque([root])
        while queue:
            level_size = len(queue)
            minimum_depth += 1
            for _ in range(level_size):
                curr = queue.popleft()

                if not curr.left and not curr.right:
                    return minimum_depth

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        return -1

    bfs(root)
    return minimum_depth


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

    print(min_depth(tree))
