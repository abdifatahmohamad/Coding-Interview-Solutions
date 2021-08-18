from typing import List


class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head: LinkedList) -> None:
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# O(N) Time || O(1) Space
def insertAtTail(arr: List[str]) -> LinkedList:
    head = LinkedList(arr)
    if head is None:
        return "The list is empty!"

    head = LinkedList(arr[0])
    for i in arr[1:]:
        last_node = head
        while last_node.next:
            last_node = last_node.next
        last_node.next = LinkedList(i)
    return head

# O(N + M) Time || O(1) Space


def find_merge_node(headA: LinkedList, headB: LinkedList) -> int:
    # Return the length both LinkedList and store it in a variable
    m = length(headA)
    n = length(headB)

    # Edge case 1: if headA is longer list than headB
    if m > n:
        # HeadA will have a higher value
        return get_node(m - n, headA, headB)
    else:
        # HeadB will have a higher value
        return get_node(n - m, headB, headA)


# Get the length of LinkedList
def length(head: LinkedList) -> int:
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count


# Get the common node
def get_node(d, headA, headB):
    # Traverse up to d in the longer LinkedList
    for _ in range(d):
        # Walk through d nodes of longer list
        headA = headA.next

    # Now headA and headB are equal distance from the merge point
    while headA != None and headB != None:
        # If not compering memory, include data
        if headA.data == headB.data:
            return headA.data
        else:
            headA = headA.next
            headB = headB.next
    # Edge case 2: if there is no merge point in the linked list at all
    return None


# arr1 = [1, 2, 3]
# arr2 = [1, 3]
arr1 = [4, 1, 6, 5, 9]
arr2 = [2, 8, 5, 9]

headA = insertAtTail(arr1)
headB = insertAtTail(arr2)

print(find_merge_node(headA, headB))

######################################################################


# This solution works if we're comparing the two linkedlist's memory:
class SinglyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: SinglyLinkedListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next


# O(N) Time || O(1) Space
def findMergeNode(headA, headB) -> int:
    currentA = headA
    currentB = headB
    while currentA != currentB:
        if currentA.next is None:
            currentA = headB
        else:
            currentA = currentA.next
        if currentB.next is None:
            currentB = headA
        else:
            currentB = currentB.next
    return currentB.val


one1 = SinglyLinkedListNode(1)
two1 = SinglyLinkedListNode(2)
three1 = SinglyLinkedListNode(3)
print("Address of four here:", id(three1))

one2 = SinglyLinkedListNode(1)
three2 = SinglyLinkedListNode(3)
three2 = three1  # Assign memory address three1 same as memory address three2
print("Address of four here:", id(three2))

headA = SinglyLinkedListNode("*")
headA.next = one1
headA.next.next = two1
headA.next.next.next = three1
headA = headA.next
print_list(headA)
print()

headB = SinglyLinkedListNode("*")
headB.next = one2
headB.next.next = three2
# headB.next.next.next = None
headB = headB.next
print_list(headB)
print()
print("The merge point of the two linked list is: ", findMergeNode(headA, headB))

# Address of four here: 140188891369824
# Address of four here: 140188891369824
# 1 -> 2 -> 3 ->
# 1 -> 3 ->
# The merge point of the two linked list is:  3
