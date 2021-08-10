class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head: LinkedList) -> None:
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


def insertAtTail(head: LinkedList, data) -> LinkedList:
    new_node = LinkedList(data)
    # Case 1: if head pointer is None
    if head is None:
        head = new_node
    else:
        # Case 2: Insert node at the tail
        last_node = head
        # Traverse to the end of the list
        while last_node.next:
            # Move to the next pointer
            last_node = last_node.next
        # Assign the new node at the end of the tail
        last_node.next = new_node
    return head


# LL = LinkedList("A")
# LL.next = LinkedList("B")
# LL.next.next = LinkedList("C")
# print_list(LL)


node = LinkedList("A")
node = insertAtTail(node, "B")
node = insertAtTail(node, "C")
node = insertAtTail(node, "D")
node = insertAtTail(node, "E")

print_list(node)
