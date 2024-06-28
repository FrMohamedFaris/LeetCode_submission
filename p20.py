class Solution(object):
    def singleNumber(self, nums):
        num_list = {}

        for n in nums:
            if n in num_list:
                num_list[n] += 1
            else:
                num_list[n] = 1
        print(num_list)
        unique_elements = [num for num, count in num_list.items() if count == 1]

        return unique_elements


nums = [1, 2, 1, 3, 2, 5]
sol = Solution()
print(sol.singleNumber(nums))
