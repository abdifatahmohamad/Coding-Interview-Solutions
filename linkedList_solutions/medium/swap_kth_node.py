# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return None
        
        length = get_length(head)
        if k > length:
            return None
        
        front = find_kth_node_from_beginning(head, k)
        back = find_kth_node_from_end(head, k)
        front.val, back.val = back.val, front.val
        
        return head
            

def find_kth_node_from_beginning(head, k):
    curr = head
    for i in range(k - 1):
        curr = curr.next
    return curr

def find_kth_node_from_end(head, k):
    curr = head
    for i in range(get_length(head) - k):
        curr = curr.next
    return curr
                
def get_length(head):
    curr = head
    count = 0
    while curr:
        count = count + 1
        curr = curr.next
    return count
