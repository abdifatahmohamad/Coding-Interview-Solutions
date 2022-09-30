class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        [2,7,11,15], target = 9 
         ^
         9 - 2 = 7
         9 -7 = 2
            map = {
                2: 0
                7 : 1
            }
        
        '''
        map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            else:
                map[n] = i
                
        return [-1, -1]
        