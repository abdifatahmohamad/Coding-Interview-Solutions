# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            total = 0
            while head.val != 0:
                total += head.val
                head = head.next
                            
            if total > 0:
                res.append(total)
            head = head.next
            
        # Convert array into LikedList
        dummyHead = ListNode(None)
        curr = dummyHead
        for num in res:
            curr.next = ListNode(num)
            curr = curr.next

        return dummyHead.next
                
        