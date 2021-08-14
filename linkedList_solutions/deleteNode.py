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
def insertAtTail(arr: List[str]) -> LinkedList:
    head = LinkedList(arr)
    if not head:
        return "String is empty!"

    head = LinkedList(arr[0])
    for i in arr[1:]:
        last_node = head
        while last_node.next:
            last_node = last_node.next
        last_node.next = LinkedList(i)
    return head


# O(1) Time and Space
def deleteFromBeginning(head: LinkedList) -> LinkedList:
    # Case1: If there is no nodes in the list (Nothing to delete)
    if not head:
        return None

    temp = head
    # Move the head to the next position
    head = head.next
    temp = None
    return head

# O(1) Time and Space


def deleteAtEnd(head: LinkedList) -> LinkedList:
    # Case1: If there is no nodes in the list (Nothing to delete)
    if not head:
        return None

    # Identify the node prev to the node that we want to be deleted
    second_last = head
    while(second_last.next.next):
        second_last = second_last.next
    second_last.next = None
    return head


# O(N) Time || O(1) Space
def deleteNodeAtPosition(head: LinkedList, pos) -> LinkedList:
    # Case1: If there is no nodes in the list (Nothing to delete)
    if not head:
        return None

    # Function return number of nodes present in list
    def length(head: LinkedList) -> int:
        current = head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    # given index is in list or not
    length = length(head)
    if (pos >= length or pos < 0):
        print("Invalid position!")
        return None

    # Case 2: If position is 0 (Node is head of the list)
    if pos == 0:
        head = head.next
    else:
        # Identify the node prev to the node that we want to be deleted
        # (pos -1) reaches the node that is one prev to the node to be deleted
        curr_node = head
        for i in range(pos - 1):
            curr_node = curr_node.next

        # Get the node to be deleted
        nodeToDelete = curr_node.next

        # Get the address of node next to the node to be deleted
        next_node = nodeToDelete.next

        # Point the next of ptr to the nextNode
        curr_node.next = next_node

    return head


airports = ["MSP", "BOS", "ATL", "LAX"]
nodes = insertAtTail(airports)
print("The original lists are: ")
print_list(nodes)


print("\nAfter deleting node from the beginning: ")
node = deleteFromBeginning(nodes)
print_list(node)  # "MSP" will pop off

print("\nAfter deleting node at the end of the list: ")
node = deleteAtEnd(nodes)
print_list(node)  # "LAX" will pop off


print("\nAfter deleting specific node position: ")
node = deleteNodeAtPosition(nodes, -1)
print_list(node)
