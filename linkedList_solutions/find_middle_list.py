class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head: Node) -> None:
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# Function that finds middle node of the linkedList
def middle_node(head: Node) -> Node:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(5)
node.next.next.next.next = Node(6)

print("The lists are: ")
print_list(node)

print("The middle element is: ", middle_node(node))
