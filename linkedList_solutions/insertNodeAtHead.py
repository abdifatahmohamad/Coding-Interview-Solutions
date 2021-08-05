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
