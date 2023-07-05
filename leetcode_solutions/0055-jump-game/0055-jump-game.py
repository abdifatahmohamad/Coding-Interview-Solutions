class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            # nums[i] is gonna be the jump length
            if i + nums[i] >= last_position: # If it's true, that means we can reach the gaol
                # Update/shift the goal closer to the beginning of the list
                last_position = i
                
        return last_position == 0


    
        