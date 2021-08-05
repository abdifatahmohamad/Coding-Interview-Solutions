class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head is not None:
        print(head.val, end=" -> ")
        if head.next is None:
            print("None")
            break
        head = head.next


def convertToLinkedList(arr) -> LinkedList:
    if len(arr) == 0:
        return

    head = LinkedList(arr[0])
    for i in arr[1:]:
        last_node = head
        while last_node.next:
            last_node = last_node.next
        last_node.next = LinkedList(i)
    return head


nums = [1, 2, 3, 4, 5]
n = convertToLinkedList(nums)
print_list(n)
