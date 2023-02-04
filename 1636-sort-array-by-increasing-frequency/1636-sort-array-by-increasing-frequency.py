class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)

        heap = []
        for n in frequency:
            heap.append((frequency.get(n), n))

        heap.sort(key=lambda x: (-x[0], x[1]))
        j = 0
        for i, n in heap:
            while i > 0:
                nums[j] = n
                j += 1
                i -= 1

        # Reverse the list
        res = [0 for _ in range(len(nums))]
        idx = 0
        i = len(nums) - 1
        while i >= 0:
            res[idx] = nums[i]
            idx += 1
            i -= 1
        return res