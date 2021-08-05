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


node = LinkedList("MSP")
node.next = LinkedList("ORD")
node.next.next = LinkedList("ATL")

print_list(node)  # MSP -> ORD -> ATL -> None
