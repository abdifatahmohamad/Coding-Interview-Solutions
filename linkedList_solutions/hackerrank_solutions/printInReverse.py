# Mo Solution:
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head:
        print(head.val, end="->")
        head = head.next


def reverse_list(head: LinkedList) -> LinkedList:
    curr_node = head
    prev_node = None
    while curr_node:
        temp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = temp
    head = prev_node
    print()
    print_list(head)


node = LinkedList("MSP")
node.next = LinkedList("ORD")
node.next.next = LinkedList("ATL")

print_list(node)

reverse_list(node)
