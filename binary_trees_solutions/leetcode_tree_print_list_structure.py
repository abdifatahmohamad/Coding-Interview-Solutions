import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def print_tree_bfs(root):
    if not root:
        return
    queue = collections.deque([root])
    res = []
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            curr = queue.popleft()
            res.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
    return res


if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]

    '''
            3
           /  \
          9    20
              /  \
             15   7 
    '''
    # The whole playlist: https://www.youtube.com/watch?v=cpgAULF6Vpw&list=PL7g1jYj15RUOjoeZAJsWjwV8XUo9r0hwc
    # https://www.youtube.com/watch?v=NEq_zWZWu_U&list=PL7g1jYj15RUOjoeZAJsWjwV8XUo9r0hwc&index=9
    
    tree = TreeNode(3)
    tree.left = TreeNode(9, None, None)
    tree.right = TreeNode(20, TreeNode(15, None, None),
                          TreeNode(7, None, None))
    print(print_tree_bfs(tree))  # [3, 9, 20, 15, 7]
