class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        1. Merge consecutive numbers (one pass is enough to check for all possible consecutive numbers)
        2. Move all zeros to the right

        time: O(n)
        space: O(1)
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        l, r = 0, 0
        while(r < len(nums)):
            # only move l if nums[l] != 0
            if nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
                # check if the swapped number is 0
                if nums[l] != 0:
                    l += 1

            else:
                l += 1
                r += 1

        return nums