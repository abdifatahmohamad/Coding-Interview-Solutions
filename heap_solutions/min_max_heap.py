import heapq


def min_heap(heights):
    heap = []
    for height in heights:
        heapq.heappush(heap, height)

    res = []
    while heap:
        res.append(heapq.heappop(heap))

    return res


print(min_heap([155, 185, 150]))  # [150, 155, 185]


def max_heap(heights):
    heap = []
    for height in heights:
        heapq.heappush(heap, -height)

    res = []
    while heap:
        h = heapq.heappop(heap) * -1
        res.append(h)

    return res


print(max_heap([155, 185, 150]))  # [185, 155, 150]
