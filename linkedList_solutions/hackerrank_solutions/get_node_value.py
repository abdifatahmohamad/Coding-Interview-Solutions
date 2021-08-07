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


def getNode(head: LinkedList, pos) -> LinkedList:
    leng = get_length(head) - 1
    if pos > leng:
        return "Invalid Position."

    length = leng - pos
    curr_node = head
    while length > 0:
        length -= 1
        curr_node = curr_node.next
    return curr_node.val


# Func/method that gets the length of the list
def get_length(head):
    curr_node = head
    count = 0
    while curr_node is not None:
        curr_node = curr_node.next
        count += 1
    return count


airports = ["MSP", "BOS", "ATL", "LAX"]
nodes = insertAtTail(airports)
# print("The length of the list is: ", get_length(nodes))
# print_list(nodes)
print(getNode(nodes, 2))
