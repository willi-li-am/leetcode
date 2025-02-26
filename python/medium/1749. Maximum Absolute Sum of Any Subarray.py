class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        one for largest positive, one for largest negative, compare
        Positive: if ever our curr sum is negative, it's better to just take the next number rather than continuing
        Negative: same idea but if sum is positive, better to take next number

        time: O(n)
        space: O(1)
        """
        curr_positive = 0
        curr_negative = 0
        max_positive = 0
        max_negative = 0
        for num in nums:
            if curr_positive < 0:
                curr_positive = num
            else:
                curr_positive += num

            if curr_negative > 0:
                curr_negative = num
            else:
                curr_negative += num
            
            max_positive = max(max_positive, curr_positive)
            max_negative = min(max_negative, curr_negative)

        return max(max_positive, -max_negative)