class Solution(object):
    def minimizedMaximum(self, n, quantities):

        quantities.sort()

        low, high = 1, max(quantities)

        while low < high:
            mid = (low + high) // 2
            count = 0
            for i in quantities:
                count += (i + mid - 1) // mid
                if count > n:
                    break

            if count <= n:
                high = mid
            else:
                low = mid + 1

        return low


n = 7
quantities = [15, 10, 10]
sol = Solution()
print(sol.minimizedMaximum(n, quantities))
