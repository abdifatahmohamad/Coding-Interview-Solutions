# Covert array into linkedList

# Let's say you have:
res = [4, 11]


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def convert_array_into_linkedList(lst):
    dummyHead = ListNode(-1)
    curr = dummyHead
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next

    return dummyHead.next
