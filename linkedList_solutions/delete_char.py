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


def delete_char(head: LinkedList, ch):
    # Case1: If there is no characters in the list (Nothing to delete).
    if head == None:
        return head

    # Case 2: If character is the head of the list.
    if ch == 0:
        head = head.next
    else:
        # Case 3: If character is in anywhere in the list.
        counter = 1
        curr_node = head
        while curr_node and counter < ch:
            # Keep looping through the list
            curr_node = curr_node.next
            counter += 1

        # Check if given char not found in list
        if curr_node is None:
            print("Invalid character!")
            return

        # Case3: Delete the given character
        curr_node.next = curr_node.next.next
    return head


string = "somalia"
nodes = insertAtTail(string)
print("The original lists are: ")
print_list(nodes)
print("\nLinked List after Deletion at specific character.")
node = delete_char(nodes, 3)
print_list(node)
