# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use two pointers
        curr, prev = head, None
        while curr:
            # Reverse pointers
            # Temp holds the pointer of current node
            temp = curr.next
            curr.next =  prev
            # Now prev became the new head pointer
            prev = curr
            curr = temp
        return prev
        