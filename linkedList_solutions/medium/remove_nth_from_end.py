from typing import List


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def insertAtTail(arr: List[int]) -> ListNode:
    head = ListNode(arr)
    if not head:
        print("List is empty.")

    head = ListNode(arr[0])
    for i in arr[1:]:
        last_node = head
        while last_node.next:
            last_node = last_node.next
        last_node.next = ListNode(i)
    return head


def remove_nth_node(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = head
    while n > 0 and fast is not None:
        fast = fast.next
        n -= 1

    while fast is not None:
        fast = fast.next
        slow = slow.next

    # Delete the node
    slow.next = slow.next.next
    # Send deleted note to the garbage collection
    slow = None

    return dummy.next


lst = [7, 3, 9, 2, 5, 0]
nodes = insertAtTail(lst)
print("The original lists are: ")
print_list(nodes)

print("\nAfter removing specific nth node: ")
node = remove_nth_node(nodes, 3)
print_list(node)
