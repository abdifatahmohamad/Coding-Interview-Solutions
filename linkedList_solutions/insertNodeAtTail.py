from typing import List


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" -> ")
        if head.next is None:
            print("None")
            break
        head = head.next


# O(N) Time || O(1) Space
def insertNodeAtTail(head, val) -> LinkedList:
    new_node = LinkedList(val)
    if head is None:
        head = new_node

    last_node = head
    while last_node.next is not None:
        last_node = last_node.next
    last_node.next = new_node
    return head


node = LinkedList("MSP")
node = insertNodeAtTail(node, "ORD")
node = insertNodeAtTail(node, "BOS")
node = insertNodeAtTail(node, "MIA")

print_list(node)


# Solution 2: inserting nodes as an array and then converting into a linked List:
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" -> ")
        if head.next is None:
            print("None")
            break
        head = head.next


# O(N) Time || O(1) Space
def insertAtTail(arr: List[str]) -> LinkedList:
    head = LinkedList(arr)
    if head is None:
        return

    head = LinkedList(arr[0])
    for i in arr[1:]:
        last_node = head
        while last_node.next:
            last_node = last_node.next
        last_node.next = LinkedList(i)
    return head


airports = ["MSP", "LAX", "ORD", "SDF", "BOS"]
nodes = insertAtTail(airports)
print_list(nodes)

#####################################################################


# The above solution but using helper func
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" -> ")
        if head.next is None:
            print("None")
            break
        head = head.next


# O(N^2) Time || O(1) Space
def insertAtTail(arr: List[str]) -> LinkedList:
    # Assign the first element in the list to be the head
    head = LinkedList(arr[0])

    # Since the first element is the head we start at index 1
    for node in arr[1:]:
        helper_function(head, node)
    return head


def helper_function(head: LinkedList, node) -> None:
    # we will insert all the nodes at the end of the linked list
    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = LinkedList(node)


airports = ["MSP", "LAX", "ORD", "SDF", "BOS"]
nodes = insertAtTail(airports)
print_list(nodes)
