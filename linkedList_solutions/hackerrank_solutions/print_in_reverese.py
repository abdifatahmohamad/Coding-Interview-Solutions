class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.stack = []
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

    # Method that prints the list in reverse
    # https://www.youtube.com/watch?v=e6YGwK5y7MQ
    def reversePrint(self):
        # Case1: Head is NULL
        if self.head == None:
            return

        # Case2: Head is NOT NULL
        # Use another data structure "stack" which adds the node to the stack each time
        curr_node = self.head
        while curr_node != None:
            self.stack.append(curr_node)
            curr_node = curr_node.next
        # While sack in NOT empty
        while self.stack:
            node = self.stack.pop()
            print(node.data, end=" <- ")

    # This method prints the elements of the linkedList
    def printLinkedList(self):
        # Case1: Check if the list is NOT null
        if self.head is None:
            print("The list is empty!")

        # Case2: If there is some values in the list
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" -> ")  # Insert at the tail
            curr_node = curr_node.next
        print()


LL = SinglyLinkedList()
LL.insertNodeAtHead("MSP")
LL.insertNodeAtHead("ORD")
LL.insertNodeAtHead("ATL")
LL.insertNodeAtHead("BOS")
LL.insertNodeAtHead("MIA")
print("################# Print original list ###################")
LL.printLinkedList()

print("################# Print in revere the list ###################")
LL.reversePrint()
