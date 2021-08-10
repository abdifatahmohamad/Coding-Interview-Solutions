class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head: LinkedList) -> None:
    while head:
        print(head.val, end=" -> ")
        if head.next is None:
            print("None")
            break
        head = head.next

# # Insert node at Head
# def insertNodeAtHead(head: LinkedList, val) -> LinkedList:
#     new_node = LinkedList(val)
#     if head is not None:
#         new_node.next = head
#     head = new_node
#     return head

# Insert node at Tail


def insertNodeAtTail(head: LinkedList, val) -> LinkedList:
    new_node = LinkedList(val)
    if head is None:
        head = new_node

    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
    return head


def deleteNode(head: LinkedList, position) -> LinkedList:
    # Case1: If there is no nodes in the list (Nothing to delete)
    if head == None:
        return head

    # Case 2: If position is 0 (Node is head of the list)
    if position == 0:
        head = head.next
    else:
        # Case 3: If position is anywhere in the list (other head of the list)
        counter = 1
        curr_node = head
        while curr_node and counter < position:  # We could start counter at 1, and pos -1
            # Keep looping through the list
            curr_node = curr_node.next
            counter += 1

        # Check if we exceeded the pos (higher pos)
        if curr_node is None:
            print("Invalid position!")
            return

        # Case3: Delete the node when it reaches particular position
        curr_node.next = curr_node.next.next
    return head


# Insert node at Head
# node = LinkedList("MSP")
# node = insertNodeAtHead(node, "ORD")
# node = insertNodeAtHead(node, "ATL")
# node = insertNodeAtHead(node, "SDF")
# node = insertNodeAtHead(node, "BOS")
# print_list(node)
# Insert node at Tail
node = LinkedList("MSP")
node = insertNodeAtTail(node, "ORD")
node = insertNodeAtTail(node, "ATL")
node = insertNodeAtTail(node, "SDF")
node = insertNodeAtTail(node, "BOS")
print("The original lists are: ")
print_list(node)

print("After deleting specific node position: ")
node = deleteNode(node, 3)  # "SDF" will pop off
print_list(node)

#######################################################################
# Insertion nodes as an array:


# O(N^2) Time || O(1) Space
def insertAtTail(arr: List[str]) -> LinkedList:
    head = LinkedList(arr[0])

    for node in arr[1:]:
        helper_function(head, node)
    return head


def helper_function(head: LinkedList, node) -> None:
    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = LinkedList(node)


def deleteNode(head: LinkedList, position) -> LinkedList:
    # Case1: If there is no nodes in the list (Nothing to delete)
    if head == None:
        return head

    # Case 2: If position is 0 (Node is head of the list)
    if position == 0:
        head = head.next
    else:
        # Case 3: If position is anywhere in the list (other head of the list)
        counter = 1
        curr_node = head
        while curr_node and counter < position:  # We could start counter at 1, and pos -1
            # Keep looping through the list
            curr_node = curr_node.next
            counter += 1

        # Check if we exceeded the pos (higher pos)
        if curr_node is None:
            print("Invalid position!")
            return

        # Case3: Delete the node when it reaches particular position
        curr_node.next = curr_node.next.next
    return head


airports = ["MSP", "BOS", "ATL", "LAX"]
nodes = insertAtTail(airports)
print("The original lists are: ")
print_list(nodes)
print("After deleting specific node position: ")
node = deleteNode(nodes, 2)
print_list(node)  # "ATL" will pop off
