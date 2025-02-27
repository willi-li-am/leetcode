class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Make an array where it has the length of each section of consecutive 0s and 1s

        time: O(n)
        space: O(n) (sliding window is O(1))
        """
        lengths = []
        is_zero = None
        first_zero = None
        for num in nums:
            if is_zero != None and (is_zero and num == 0 or not is_zero and num == 1):
                lengths[-1] += 1
            elif is_zero == None:
                first_zero = num == 0
                is_zero = num == 0
                lengths.append(1)
            else:
                is_zero = num == 0
                lengths.append(1)

        zero = 0 if first_zero else 1

        res = 0

        for i in range(len(lengths)):
            length = lengths[i]
            total = 0

            if i % 2 == zero:
                total = 1
                if length == 1:
                    if i > 0:
                        total += lengths[i - 1]
                    if i < len(lengths) - 1:
                        total += lengths[i + 1]
            else:
                total = length
                if i > 0 or i < len(lengths) - 1:
                    total += 1
            res = max(res, total)

        return res