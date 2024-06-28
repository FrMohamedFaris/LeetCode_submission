from collections import Counter


class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        count = Counter(arr1)

        result = []

        for a in arr2:
            if a in count:
                result.extend([a] * count[a])
                del count[a]

        remain = sorted(count.elements())
        result.extend(remain)

        return result


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
sol = Solution()
print(sol.relativeSortArray(arr1, arr2))
