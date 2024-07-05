import heapq


class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 4:
            return 0

        smallest = heapq.nsmallest(4, nums)
        largest = heapq.nlargest(4, nums)
        ans = float('inf')
        for i in range(4):
            ans = min(ans, largest[i] - smallest[3 - i])

        return ans


nums = [1, 5, 0, 10, 14]
sol = Solution()
print(sol.minDifference(nums))
