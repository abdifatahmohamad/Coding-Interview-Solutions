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

######################################################################

    def insertAtTail(self, val):
        # Case1: create new node that consist of data
        new_node = Node(val)

        # Case2: if check if the list is NOT NULL
        if self.head is None:
            self.head = new_node
            return

        # Case3: check if there is some values in the list
        last_node = self.head
        while last_node.next:
            # Move the head pointer to the right
            last_node = last_node.next
        last_node.next = new_node

######################################################################

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

######################################################################

    def deleteNode(self, key):
        # Delete node that is the head of the list
        curr_node = self.head
        if self.head and curr_node.val == key:
            self.head = curr_node.next
            curr_node = None
            return

        # Delete node that is NOT head of the list
        prev_node = None
        # Loop through while head node in NOT None
        curr_node = self.head
        while curr_node and curr_node.val != key:
            prev_node = curr_node
            curr_node = curr_node.next

        # Check if the node we wanna del is NOT in the list
        if curr_node is None:
            print("Sorry, the node is NOT in the list.")
            return
        # Otherwise if the node we wanna del is in the list
        prev_node.next = curr_node.next
        curr_node = None

######################################################################
    # It's similar idea of deleting node
    def deleteNodeAtPosition(self, position):
        # Case 1: when the position is 0 (Node is head of the list)
        curr_node = self.head
        if position == 0:
            self.head = curr_node.next
            curr_node = None
            return

        # Case 2: when the position is anywhere in the list (other head of the list)
        count = 0
        prev_node = None
        curr_node = self.head
        while curr_node and count != position:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        if curr_node is None:
            print(
                "The position was greater than the number of elements in the list.")
            return
        prev_node.next = curr_node.next
        curr_node = None


######################################################################


    def printList(self):
        # Case1: check first if the head is NOT NULL
        if self.head is None:
            print('The list is empty')
            return

        # Case2: if there is some values in list
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val, end=" -> ")  # Insert at the tail
            # print(curr_node.val, end=" <- ") # Insert at the head
            curr_node = curr_node.next
        print()

######################################################################


node = LinkedList()

node.insertAtHead("MSP")
node.insertAtTail("ATL")
node.insertAtTail("BOS")
node.insertAtHead("LAX")
node.insertAtTail("MIA")

node.printList()

# print(node.head.val)  # This will print our head node
# print(node.head.next.val)  # This will print our next node after the head
# This is insert ORD in between MSP and ATL
node.insertAfterNode(node.head.next, "ORD")
print("\n")
print("################# Inserting 'ORD' in the list ###################")
node.printList()


print("\n")
print("################# Deleting 'ATL' from the list ###################")
# Delete "BOS" in the list
node.deleteNode("ATL")
node.printList()

print("\n")
print("################# Deleting at pos 1 from the list ###################")
# Delete at pos "MSP" in the list
node.deleteNodeAtPosition(1)
node.printList()
