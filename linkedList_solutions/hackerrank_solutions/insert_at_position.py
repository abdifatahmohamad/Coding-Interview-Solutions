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


def insertNodeAtPosition(head: LinkedList, data, pos):
    # Create new node
    new_node = LinkedList(data)

    # If the head pointer is None
    if head is None:
        head = new_node
    else:
        curr_node = head
        # Skip the node to reach at position
        count = 1
        while curr_node and count < pos:
            # Move the pointer forward
            curr_node = curr_node.next
            count += 1

            # Check if curr_node is NULL
            if curr_node is None:
                print("Invalid position!")
        # Insert the node(assign the next pointer of new_node to the next pointer of curr_node. Then assign curr_node pointer to the new node)
        new_node.next = curr_node.next
        curr_node.next = new_node
    return head


node = LinkedList("A")
node = insertAtTail(node, "B")
node = insertAtTail(node, "D")
node = insertAtTail(node, "E")

node = insertNodeAtPosition(node, "C", 1)  # A -> C -> B -> D -> E -> None

print_list(node)
