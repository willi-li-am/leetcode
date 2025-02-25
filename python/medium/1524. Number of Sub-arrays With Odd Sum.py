# Optimal Solution (First solution under)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        We don't need previous sums, so we can just keep track of current sum (similar to prefix sum solution)

        time: O(n)
        space: O(1)
        """
        num_odds = 0
        num_evens = 0

        res = 0

        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum % 2 == 0:
                res += num_odds
                num_evens += 1
            else:
                res += 1
                res += num_evens
                num_odds += 1

        return res % (1000000007)


# First solution (double pass), we can do a single pass by combining prefix sum with the loop

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        prefix sum, then we loop and keep track of odd and even sums
        odd & even give odd

        [1, 3, 5] -> [1, 4, 9]

        time: O(n)
        space: O(n)
        """

        prefix = []
        for i in range(len(arr)):
            if i == 0:
                prefix.append(arr[i])
            else:
                prefix.append(arr[i] + prefix[i - 1])

        num_odds = 0
        num_evens = 0

        res = 0

        for i in range(len(prefix)):
            if prefix[i] % 2 == 0:
                res += num_odds
                num_evens += 1
            else:
                res += 1
                res += num_evens
                num_odds += 1

        return res % (1000000007)
    
