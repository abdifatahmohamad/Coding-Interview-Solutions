# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def linked_list_to_array(head):
            array = []
            current = head

            while current:
                array.append(current.val)
                current = current.next

            return array

        array = linked_list_to_array(head)
        i = 0
        j = len(array) - 1
        max_sum = float('-inf')

        while i < j:
            current_sum = array[i] + array[j]
            max_sum = max(max_sum, current_sum)
            i += 1
            j -= 1

        return max_sum
    
    
        