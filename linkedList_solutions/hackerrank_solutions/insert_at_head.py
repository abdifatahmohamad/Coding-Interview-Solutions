class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method that inserts the node at the tail
    def insertNodeAtHead(self, data):
        # Case1: Create new node that consist of data
        new_node = SinglyLinkedListNode(data)
        # Case2: Change the next component/field of the new node to point to the head of the list
        if self.head != None:
            new_node.next = self.head
        # Move the head node to the new node
        self.head = new_node

    # This method prints the elements of the linkedList
    def printLinkedList(self):
        # Case1: Check if the list is NOT null
        if self.head is None:
            print("The list is empty!")

        # Case2: If there is some values in the list
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" <- ")  # Insert at the head
            curr_node = curr_node.next
        print()


LL = SinglyLinkedList()
LL.insertNodeAtHead(321)
LL.insertNodeAtHead(975)
LL.insertNodeAtHead(392)
LL.insertNodeAtHead(484)
LL.insertNodeAtHead(383)

LL.insertNodeAtHead(9000)

LL.printLinkedList()
