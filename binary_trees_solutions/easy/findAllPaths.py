import collections


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def find_paths(tree):
    paths = []

    def dfs(root, curr_path):
        if not root:
            return

        curr_path.append(root.val)

        if not root.left and not root.right:
            paths.append(list(curr_path))
            return

        dfs(root.left, curr_path)
        dfs(root.right, curr_path)

        curr_path.pop()

    dfs(tree, [])
    return paths


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
    nodes = [1, 2, 3, 3, 8, 8, 5, None, 4, 4, None, 4, 3, 3, None, None, None, None, 5, None, 5, None, None, None, 5, 5,
             None, 5, None, None, None]

    tree = create_tree(nodes)
    print(find_paths(tree))
