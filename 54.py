class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-2):

            left,right =  i + 1 ,n-1


nums = [-1, 2, 1, -4]
target = 1
sol = Solution()
print(sol.threeSumClosest(nums, target))
