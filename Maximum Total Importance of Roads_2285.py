from collections import defaultdict


class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        pairs = [0] * n
        for i, j in roads:
            pairs[i] += 1
            pairs[j] += 1
        pairs.sort(reverse=True)
        count = 0
        for i in range(n):
            count += pairs[i] * (n - i)
        return count


n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
sol = Solution()
print(sol.maximumImportance(n, roads))
