class Solution(object):
    def heightChecker(self, heights):
        sorted_arr = sorted(heights)

        count = sum(1 for i in range(len(sorted_arr)) if heights[i] != sorted_arr[i])

        return count


heights = [2, 1, 2, 1, 1, 2, 2, 1]
sol = Solution()
print(sol.heightChecker(heights))
