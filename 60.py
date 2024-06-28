from collections import deque


class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        flip_deque = deque()

        for i in range(n):
            if flip_deque and flip_deque[0] <= i - k:
                flip_deque.popleft()

            if len(flip_deque) % 2 == nums[i]:
                if i + k > n:
                    return -1

                flip_deque.append(i)
                count += 1

        return count


nums = [0, 1, 0]
k = 1
sol = Solution()
print(sol.minKBitFlips(nums, k))
