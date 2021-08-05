from typing import List


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next


def convert_to_linkedlist(arr: List[str]) -> LinkedList:
    # Assign the first element in the list to be the head
    head = LinkedList(arr[0])

    # Since the first element is the head we start at index 1
    for node in arr[1:]:
        convert_to_linkedlist_helper(head, node)
    return head


def convert_to_linkedlist_helper(head: LinkedList, node) -> None:
    # we will insert all the nodes at the end of the linked list
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = LinkedList(node)


airports = ["MSP", "LAX", "ORD", "SDF", "BOS"]
nodes = convert_to_linkedlist(airports)
print_list(nodes)
