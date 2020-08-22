# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def reverseLinkedList(head):
	curr, prev = head, None 
	while curr is not None:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
	return prev
