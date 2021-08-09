class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head:
        print(head.val, end=" -> ")
        if head.next is None:
            print("None")
            break
        head = head.next


# Iterative solution
def get_length(head: LinkedList) -> int:
    current = head
    count = 0
    while current is not None:
        current = current.next
        count += 1
    return count


# Recursive solution
def get_length(head: LinkedList) -> int:
    # Base case
    if head is None:
        return 0

    return 1 + get_length(head.next)


L1 = LinkedList(1)
L1.next = LinkedList(2)
L1.next.next = LinkedList(3)
L1.next.next.next = LinkedList(4)

print(get_length(L1))
