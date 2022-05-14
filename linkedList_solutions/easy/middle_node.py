# https://www.youtube.com/watch?v=sGdwSH8RK-o
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


def middle_node(head: ListNode) -> int:
    count = 0
    while head:
        head = head.next
        count += 1

    curr = head
    # mid = get_length(head) // 2
    mid = count // 2
    for i in range(mid):
        curr = curr.next
    return curr


# def get_length(head: ListNode) -> int:
#     count = 0
#     while head:
#         head = head.next
#         count += 1
#     return count


nums = [1, 2, 3, 4, 5]
nodes = insertAtTail(nums)
print_list(nodes)

print(middle_node(nodes))

# print(get_length(nodes))
