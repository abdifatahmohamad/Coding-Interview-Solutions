class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, c in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            # If the count is 0, we don't wanna add to the heap
            if count != 0:
                heapq.heappush(heap, (count, c))

        res = []
        while heap:
            freq, ch = heapq.heappop(heap)  # Taking the most common character
            if len(res) >= 2 and res[-1] == res[-2] == ch:  # If the character has been used twice already
                if not heap:  # If there are no other characters available, return the result
                    return "".join(res)
                count, char = heapq.heappop(heap)  # Taking the second most common character
                heapq.heappush(heap, (freq, ch))  # Put the first character back in the heap
                freq, ch = count, char  # Swap the character count
            res.append(ch)  # Add the character to the result
            freq += 1  # Decrement the character count
            if freq < 0:  # If the count is not zero, put the character back in the heap
                heapq.heappush(heap, (freq, ch))

        return "".join(res)
        