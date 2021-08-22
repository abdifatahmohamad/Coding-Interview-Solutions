class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# O(N) Time || O(1) Space
def remove_duplicates(head: ListNode) -> ListNode:
    if not head:
        return "The list is empty!"

    # Create a temp variable that does all traversal work
    current = head
    while current and current.next:
        if current.val == current.next.val:
            # Skip duplicate values
            current.next = current.next.next
        else:
            # move to the next node (keep traversing)
            current = current.next
    return head

##########################################################################


# O(N) Time || O(N) Space
def remove_duplicates(head: ListNode) -> ListNode:
    if not head:
        return "The list is empty!"

    curr = head
    prev = None
    mapping = dict()

    while curr:
        if curr.val in mapping:
            # Remove duplicate values
            prev.next = curr.next
            # Garbage collection
            curr = None
        else:
            # First time seen this element, add to the dictionary
            mapping[curr.val] = 1
            # Update previous node
            prev = curr
        # If we don't hit both if/else statement
        curr = prev.next
    return head

##########################################################################


# O(N) Time || O(N) Space
def remove_duplicates(head: ListNode) -> ListNode:
    if not head:
        return "The list is empty!"

    curr = head
    prev = None
    new_list = []  # Lookups for the list would be O(n)

    while curr:
        if curr.val not in new_list:
            # First time we encounter this element, append to the new list
            new_list.append(curr.val)
            # Update previous node
            prev = curr
        else:
            # Remove duplicate values
            prev.next = curr.next
            curr = curr.next
            # Garbage collection
            curr = None

        # If we don't hit both if/else statement
        curr = prev.next

    return head


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(2)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(3)
node.next.next.next.next.next = ListNode(3)
node.next.next.next.next.next.next = ListNode(3)

# Input: 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 3 -> None
# Output: 1 -> 2 -> 3 -> None

print_list(remove_duplicates(node))
