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

    # Method that inserts the node at the tail
    def reverse(self):
        curr, prev = self.head, None
        while curr != None:
            temp = curr.next
            # Change the direction of the nodes
            curr.next = prev
            # Shifting the nodes
            prev = curr
            curr = temp
        self.head = prev
        # return prev # HackerRank wants to return an INTEGER_SINGLY_LINKED_LIST

    # This method prints the elements of the linkedList
    def printLinkedList(self):
        # Case1: Check if the list is NOT null
        if self.head is None:
            print("The list is empty!")

        # Case2: If there is some values in the list
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" <- ")  # Insert at the tail
            curr_node = curr_node.next
        print()


LL = SinglyLinkedList()
LL.insert_node_AtTail("MSP")
LL.insert_node_AtTail("ORD")
LL.insert_node_AtTail("ATL")
LL.insert_node_AtTail("BOS")
LL.insert_node_AtTail("MIA")
print("################# Print original list ###################")
LL.printLinkedList()

print("################# Print revere the list ###################")
LL.reverse()
LL.printLinkedList()
