from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        inter = c1 & c2

        return list(inter.elements())


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
sol = Solution()
print(sol.intersect(nums1, nums2))
