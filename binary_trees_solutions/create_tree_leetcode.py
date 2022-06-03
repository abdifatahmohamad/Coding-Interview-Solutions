import collections


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


def create_tree(arr):
    num_queue = collections.deque()
    for num in arr[1:]:
        num_queue.append(num)

    queue = collections.deque()
    root = TreeNode(arr[0])
    queue.append(root)

    while num_queue:
        left_val = None if not num_queue else num_queue.popleft()
        right_val = None if not num_queue else num_queue.popleft()
        current = queue.popleft()
        if left_val:
            left = TreeNode(left_val)
            current.left = left
            queue.append(left)
        if right_val:
            right = TreeNode(right_val)
            current.right = right
            queue.append(right)
    return root


if __name__ == "__main__":
    tree = create_tree([1, 2, 3, 4, 5])
    inorder_traversal(tree)

'''
         1
        / \
       2   3
      / \
     4   5
'''
