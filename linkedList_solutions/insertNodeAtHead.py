from typing import List


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" <- ")
        if head.next is None:
            print("None")
            break
        head = head.next


# O(1) Time and Space
def insertNodeAtHead(head, val) -> LinkedList:
    new_node = LinkedList(val)
    if head != None:
        new_node.next = head
    head = new_node
    return head


node = LinkedList("MSP")
node = insertNodeAtHead(node, "ORD")
node = insertNodeAtHead(node, "BOS")
node = insertNodeAtHead(node, "MIA")

print_list(node)


# Solution 2: inserting nodes as an array and then converting into a linked List:
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" <- ")
        if head.next is None:
            print("None")
            break
        head = head.next


# O(N) Time || O(1) Space
def insertAtHead(arr: List[str]) -> LinkedList:
    head = LinkedList(arr[0])
    for i in arr[1:]:
        new_node = LinkedList(i)
        new_node.next = head
        head = new_node
    return head


airports = ["MSP", "LAX", "ORD", "SDF", "BOS"]
nodes = insertAtHead(airports)
print_list(nodes)

#####################################################################


# The above solution but using helper func
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" <- ")
        if head.next is None:
            print("None")
            break
        head = head.next


# O(N) Time || O(1) Space
def insertAtHead(arr: List[str]) -> LinkedList:
    # Assign the first element in the list to be the head
    head = LinkedList(arr[0])

    # Since the first element is the head we start at index 1
    for node in arr[1:]:
        head = helper_function(head, node)
    return head


def helper_function(head: LinkedList, node) -> LinkedList:
    # we will insert all the nodes at the end of the linked list
    new_node = LinkedList(node)
    new_node.next = head
    head = new_node
    return head


airports = ["MSP", "LAX", "ORD", "SDF", "BOS"]
nodes = insertAtHead(airports)
print_list(nodes)
