class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Initial thought process: We use nums and it's index to keep track of if a number has been seen
        but we might lose information

        solution: negative = seen (so we still keep information of number while also marking index)

        time: O(n)
        space: O(1)
        """
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        
        for num in nums:
            abs_num = abs(num)
            if abs_num > 0 and abs_num <= len(nums) and nums[abs_num - 1] > 0:
                nums[abs_num - 1] = -nums[abs_num - 1]
                
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1