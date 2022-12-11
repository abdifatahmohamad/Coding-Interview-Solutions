# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None)
        curr = dummy_head
        while head:
            total = 0
            while head.val != 0:
                total += head.val
                head = head.next
                            
            if total > 0:
                curr.next = ListNode(total)
                curr = curr.next
            head = head.next
            
        return dummy_head.next
                
        