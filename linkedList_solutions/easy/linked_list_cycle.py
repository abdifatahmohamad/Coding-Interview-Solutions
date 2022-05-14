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
        insert_helper(head, i)
    return head


def insert_helper(head: ListNode, node: int) -> ListNode:
    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = ListNode(node)
    return head


def linked_list_cycle(head: ListNode) -> bool:
    curr = head
    hash_set = set()
    while curr:
        if curr in hash_set:
            return True

        hash_set.add(curr)
        curr = curr.next
    return False


nums = [3, 2, 0, 4]
head = insertAtTail(nums)
print_list(head)

three = ListNode(3)
two = ListNode(2)
zero = ListNode(0)
n_four = ListNode(4)

three.next = two
two.next = zero
zero.next = n_four
n_four.next = zero

print(linked_list_cycle(head))
