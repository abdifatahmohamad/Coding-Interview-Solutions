# https://stackoverflow.com/questions/72238064/how-to-remove-the-nth-node-from-the-end-of-the-list-reversing-the-linked-list/72239407#72239407


from typing import List


# Reverse the list first and then remove the nth node
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


def reverse_linkedList(head: ListNode) -> ListNode:
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def remove_nth_node(head: ListNode, n: int) -> ListNode:
    if not head:
        print("Head is empty.")
    elif n < 1:
        print("Invalid nth.")
    elif n == 1:
        head = head.next
    else:
        counter = 1
        curr = head
        while curr and counter < n - 1:  # nth index starts at 1 not 0
            curr = curr.next
            counter += 1

        if curr is None:
            print("Invalid nth.")

        curr.next = curr.next.next
    return head


def remove_nth_last_node(head: ListNode, n: int) -> ListNode:
    head = reverse_linkedList(head)
    head = remove_nth_node(head, n)
    return reverse_linkedList(head)


if __name__ == "__main__":
    lst = [7, 3, 9, 2, 5, 0]
    node = insertAtTail(lst)
    print("The original list: ")
    print_list(node)

    print("\nAfter removing 3rd last node: ")
    node = remove_nth_last_node(node, 3)
    print_list(node)
