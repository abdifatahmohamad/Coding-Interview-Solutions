# O(n) time | O(1) space - where n is the number of nodes in the Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head) -> None:
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


def reverseLinkedList(head):
    curr, prev = head, None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


node = Node(1)
node.next = Node(2)
node.next.next = Node(2)
node.next.next.next = Node(3)
node.next.next.next.next = Node(4)

print_list(node)
print_list(reverseLinkedList(node))
