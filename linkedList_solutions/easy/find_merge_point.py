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
###########################################################################


# Brute Force Approach: O(N^) Time || O(1) Space
def find_merge_node(headA: LinkedList, headB: LinkedList) -> int:
    m = length(headA)
    n = length(headB)

    reseter = headB
    for i in range(m):
        headB = reseter
        for j in range(n):
            if headA.data == headB.data:
                return headA.data
            else:
                headB = headB.next
        headA = headA.next

# Get the length of LinkedList


def length(head: LinkedList) -> int:
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

###########################################################################


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

#######################################################################################
# Same as above but shorter


# O(N + M) Time || O(1) Space
def find_merge_node(headA: LinkedList, headB: LinkedList) -> int:
    m = length(headA)
    n = length(headB)
    d = n - m

    # Edge case: if headA is longer lis than headB
    if m > n:
        # Swap the two LinkedList
        temp = headA
        headA = headB
        headB = temp
        d = m - n

# Traverse up to d in the longer LinkedList(Walk through d nodes of longer list)
    for _ in range(d):
        headB = headB.next

    # Now headA and headB are equal distance from the merge point
    while headA != None and headB != None:
        # Compare values but NOT the memory
        if headA.data == headB.data:
            return headA.data
        else:
            headA = headA.next
            headB = headB.next
    # Edge case: If there is no merge point at all
    return None


# Get the length of LinkedList
def length(head: LinkedList) -> int:
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count


#######################################################################################


# arr1 = [1, 2, 3]
# arr2 = [1, 3]
arr1 = [4, 1, 6, 5, 9]
arr2 = [2, 8, 5, 9]

headA = insertAtTail(arr1)
headB = insertAtTail(arr2)

print(find_merge_node(headA, headB))
