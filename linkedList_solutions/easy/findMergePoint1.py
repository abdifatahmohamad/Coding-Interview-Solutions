class SinglyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: SinglyLinkedListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next


def find_merge_node(headA, headB) -> int:
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


one = SinglyLinkedListNode(1)
two = SinglyLinkedListNode(2)
three = SinglyLinkedListNode(3)
four1 = SinglyLinkedListNode(4)
print("Address of four here:", id(four1))

seven = SinglyLinkedListNode(7)
nine = SinglyLinkedListNode(9)
four2 = four1

print("Address of four here:", id(four2))

headA = SinglyLinkedListNode("*")
headA.next = one
headA.next.next = two
headA.next.next.next = three
headA.next.next.next.next = four1
headA = headA.next
print_list(headA)
print()

headB = SinglyLinkedListNode("*")
headB.next = seven
headB.next.next = nine
headB.next.next.next = four2
headB.next.next.next.next = None
headB = headB.next

print_list(headB)
print()

print(find_merge_node(headA, headB))
