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


arr1 = [1, 2, 3]
arr2 = [1, 3]

headA = insertAtTail(arr1)
headB = insertAtTail(arr2)

print(find_merge_node(headA, headB))
