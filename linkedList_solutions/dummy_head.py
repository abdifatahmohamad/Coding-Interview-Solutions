# https://guides.codepath.org/compsci/Dummy-Head

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head: Node) -> None:
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# Deleting node using dummy head technique
def delete_node(head, data) -> Node:
    dummy = Node(None)  # 1
    dummy.next = head
    prev = dummy
    curr = head
    while curr != None:
        if curr.data == data:
            prev.next = curr.next  # 2
            return dummy.next  # 3
        prev = curr
        curr = curr.next
    return dummy.next  # 4


node = Node(1)
node.next = Node(2)
node.next.next = Node(4)
node.next.next.next = Node(9)

# print_list(node)

print_list(delete_node(node, 4))  # 1 -> 2 -> 9 -> None
