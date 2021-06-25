class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertAtTail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Insert after given node
    def insertAfterNode(self, prev_node, val):
        # Check if the node we need to insert after is in the list
        # Means if there is no previous node to insert after at all
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):
        if self.head is None:
            print('The list is empty')
            return
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val, end=" -> ")  # Insert at the tail
            # print(curr_node.val, end=" <- ") # Insert at the head
            curr_node = curr_node.next
        print()


node = LinkedList()

node.insertAtHead("MSP")
node.insertAtTail("ATL")
node.insertAtTail("BOS")
node.insertAtHead("LAX")
node.insertAtTail("MIA ")

node.printList()

# print(node.head.val)  # This will print our head node
# print(node.head.next.val)  # This will print our next node after the head
# This is insert ORD in between MSP and ATL
node.insertAfterNode(node.head.next, "ORD")
node.printList()
