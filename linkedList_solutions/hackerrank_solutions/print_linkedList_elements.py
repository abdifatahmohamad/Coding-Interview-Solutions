class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method that inserts the node at the tail
    def insert_node_AtTail(self, node_data):
        # Case1: Create new node that consist of new node
        node = SinglyLinkedListNode(node_data)

        # Case2: Check if list is NOT null
        if not self.head:
            self.head = node
        # Case 3: Else => if there is some values in the list
        else:
            self.tail.next = node

        self.tail = node

    # This method prints the elements of the linkedList
    def printLinkedList(self):
        # Case1: Check if the list is NOT null
        if self.head is None:
            print("The list is empty!")

        # Case2: If there is some values in the list
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next
        print()


LL = SinglyLinkedList()
LL.insert_node_AtTail(16)
LL.insert_node_AtTail(13)
LL.printLinkedList()
