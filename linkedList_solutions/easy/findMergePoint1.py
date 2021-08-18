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
