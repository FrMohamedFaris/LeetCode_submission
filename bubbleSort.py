class Solution(object):
    def sortColors(self, nums):

        n_len = len(nums)

        for i in range(n_len):
            swapped = False

            for j in range(0, n_len - i - 1):

                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:
                break

        return nums


nums = [2, 0, 2, 1, 1, 0]
sol = Solution()
print(sol.sortColors(nums))
