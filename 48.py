class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total_sum = sum(nums)
        n = len(nums)
        possible_sums = {0}

        for num in nums:
            new_sums = set()
            for s in possible_sums:
                new_sums.add(s + num)
            possible_sums.update(new_sums)

        for nA in range(1, n):  # nA must be between 1 and n-1
            if total_sum * nA % n == 0:  # check if there's an integer average
                sumA = total_sum * nA // n
                if sumA in possible_sums and sumA != total_sum:
                    return True

        return False


nums = [18, 10, 5, 3]
sol = Solution()
print(sol.splitArraySameAverage(nums))
