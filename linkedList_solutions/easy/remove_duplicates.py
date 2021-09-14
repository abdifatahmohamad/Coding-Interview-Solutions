class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Brute force solution using auxiliary data structure (Duplicate values can be anywhere in the list)
# def remove_duplicates(head: Node):
#     duplicates = {}
#     current = head
#     prev = None
#     while current:
#         if current.val in duplicates:
#             prev.next = current.next
#         else:
#             duplicates[current.val] = 1
#             prev = current
#         current = current.next
#     return head


# O(N) Time || O(1) Space (Duplicate values must be neighbors)
def remove_duplicates(head: Node) -> Node:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


node = Node(4)
node.next = Node(4)
node.next.next = Node(2)
node.next.next.next = Node(1)
node.next.next.next.next = Node(1)

# print_list(remove_duplicates1(node)) # 1 -> 4 -> 2 -> None

print_list(remove_duplicates(node))
