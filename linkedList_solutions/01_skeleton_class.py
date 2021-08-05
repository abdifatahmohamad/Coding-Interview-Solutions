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


def print_in_reverse(head: LinkedList) -> LinkedList:
    curr_node = head
    prev_node = None
    while curr_node:
        temp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = temp
    head = prev_node
    print("\nPrint in reverse:")
    print_list(head)


def insertNodeAtHead(head, val) -> LinkedList:
    new_node = LinkedList(val)
    if head != None:
        new_node.next = head
    head = new_node
    return head


node = LinkedList("MSP")
node.next = LinkedList("ORD")
node.next.next = LinkedList("ATL")

print_list(node)

print_in_reverse(node)

# InsertNodeAtHead:
node = LinkedList("MSP")
node = insertNodeAtHead(node, "ORD")
node = insertNodeAtHead(node, "BOS")
node = insertNodeAtHead(node, "MIA")
print("\nInsert node at head:")
print_list(node)
