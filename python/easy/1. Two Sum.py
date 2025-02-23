class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Going through a list of numbers we want to check whether or not we've seen a number that would sum up to the target.
        If so, we return the indices of the two numbers.

        time: O(n)
        space: O(n)
        """
        seen = {}
        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in seen:
                return [seen[wanted], i]
            
            seen[nums[i]] = i
        
        return [-1, -1]