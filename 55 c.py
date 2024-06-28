class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        average = []

        while nums:
            min_num = nums.pop(0)
            max_num = nums.pop()

            avg = (min_num + max_num) / 2.0

            average.append(avg)

        return min(average)


nums = [7, 8, 3, 4, 15, 13, 4, 1]
sol = Solution()
print(sol.minimumAverage(nums))
