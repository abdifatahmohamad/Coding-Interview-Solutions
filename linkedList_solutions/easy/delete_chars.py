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


# O(N^2) Time || O(1) Space
def insertAtTail(arr: List[str]) -> LinkedList:
    head = LinkedList(arr[0])

    for node in arr[1:]:
        helper_function(head, node)
    return head


def helper_function(head: LinkedList, node) -> None:
    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = LinkedList(node)


# O(N) Time || O(1) Space
def delete_chars(head: LinkedList, ch) -> LinkedList:
    # Case1: If there is no characters in the list (Nothing to delete).
    if head == None:
        return head

    # Case 2: If character is the head of the list.
    if head.val == ch:
        head = head.next

    # Case3: If character anywhere in the list
    curr_node = head
    while curr_node.next is not None:
        if curr_node.next.val != ch:
            # Keep looping through
            curr_node = curr_node.next
        else:
            # Delete character
            curr_node.next = curr_node.next .next
    return head


string = "somalis"
nodes = insertAtTail(string)
print("Original list: ")
print_list(nodes)
print("\nLinked List after Deletion at specific character.")
node = delete_chars(nodes, "s")
print_list(node)
