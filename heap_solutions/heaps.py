import heapq

heap = [5, 7, 9, 1, 3]

'''

        5
      /   \
     7     9
    / \
   1   3
   
   
'''

heapq.heapify(heap)

heapq.heappop(heap)
print("Pop 1 from heap:", heap)

heapq.heappop(heap)
print("Pop 3 from heap:", heap)

print(heap)  # [1, 5, 3, 9, 7]

'''
        1
      /   \
     3     9
    / \
   7   5

'''
# Append 4 to the heap
heapq.heappush(heap, 4)

print(heap)  # [1, 3, 4, 7, 5, 9]

'''
        1
      /   \
     3     4
    / \   /
   7   5 9

'''
