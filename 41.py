class Solution(object):
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1

        low, high = min(bloomDay), max(bloomDay)

        while low <high:
            mid = (low + high) // 2
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0


                if bouquets >= m:
                    break

            if bouquets >= m:
                high = mid
            else:
                low = mid + 1

        return low


bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
m = 4
k = 2
sol = Solution()
print(sol.minDays(bloomDay, m, k))
