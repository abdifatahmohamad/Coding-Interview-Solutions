from typing import List


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def compare_lists(L1: LinkedList, L2: LinkedList) -> int:
    head1 = L1
    head2 = L2

    # Check if both head pointers have some elements in the node
    while head1 != None and head2 != None:
        # Check if data are same
        if head1.val == head2.val:
            # Move both pointers forward
            head1 = head1.next
            head2 = head2.next
        else:
            return 0

    # Check both LinkedList reaches the end (Check both length)
    # if head1 == None and head2 == None:
    if head1 == head2:
        return 1
    else:
        return 0


L1 = LinkedList(1)
L1.next = LinkedList(2)
L1.next.next = LinkedList(3)

L2 = LinkedList(1)
L2.next = LinkedList(2)
L2.next.next = LinkedList(3)
# L2.next.next.next = LinkedList(4)
print(compare_lists(L1, L2))


#############################################
# Neater Solution
# O(N) Time || O(1) Space
def compare_lists(L1: LinkedList, L2: LinkedList) -> int:
    # Check edge case
    if L1 is None or L2 is None:
        return 0

    while L1 is not None and L2 is not None:
        if L1.val != L2.val:
            return 0
        L1 = L1.next
        L2 = L2.next

    # If of the lists reached None before the other than return 0
    return 1 if L1 == L2 else 0
