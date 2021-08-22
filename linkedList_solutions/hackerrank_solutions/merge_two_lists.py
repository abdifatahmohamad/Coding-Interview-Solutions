class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head: LinkedList) -> None:
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


def merge_lists(headA, headB):
    # Base case
    if not headA:
        return headB
    if not headB:
        return headA

    dummy = LinkedList(None)
    curr = dummy

    while headA != None and headB != None:
        if headA.data < headB.data:
            curr.next = headA
            headA = headA.next
        else:
            curr.next = headB
            headB = headB.next

        curr = curr.next

    if headA != None:
        curr.next = headA
    else:
        curr.next = headB

    return dummy.next


node1 = LinkedList(1)
node1.next = LinkedList(2)
node1.next.next = LinkedList(7)

node2 = LinkedList(1)
node2.next = LinkedList(3)

print_list(merge_lists(node1, node2))

#######################################################################


class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __iter__(self):
        head = self
        while head:
            yield head.data
            head = head.next
        yield None  # Optional

    def __repr__(self):
        return " -> ".join(map(str, self))


def merge_lists(headA, headB):
    # Base case
    if not headA:
        return headB
    if not headB:
        return headA

    dummy = LinkedList(None)
    curr = dummy

    while headA != None and headB != None:
        if headA.data < headB.data:
            curr.next = headA
            headA = headA.next
        else:
            curr.next = headB
            headB = headB.next

        curr = curr.next

    if headA != None:
        curr.next = headA
    else:
        curr.next = headB

    return dummy.next


node1 = LinkedList(1)
node1.next = LinkedList(2)
node1.next.next = LinkedList(7)

node2 = LinkedList(1)
node2.next = LinkedList(3)

print(merge_lists(node1, node2))

#######################################################################


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # Base case
    if not list1:
        return list2
    if not list2:
        return list1

    dummy_head = ListNode(-1)
    current = dummy_head

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            # Insert list1 to the current
            current.next = list1
            # Update list1 pointer
            list1 = list1.next
        else:
            # Insert list1 to the current
            current.next = list2
            # Update list2 pointer
            list2 = list2.next
        # Update current pointer
        current = current.next

    # If one of the lists exhausted
    if list1 is not None:
        current.next = list1
    else:
        current.next = list2

    return dummy_head.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    # print_list(l1)
    # print_list(l2)

    merged_lists = merge_two_lists(l1, l2)
    print_list(merged_lists)

    #######################################################################
