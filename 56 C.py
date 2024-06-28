class Solution(object):

    def minimunSum(self, grid):
        m, n = len(grid), len(grid[0])

        # Compute prefix sums
        prefix_sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sums[i][j] = grid[i - 1][j - 1] + prefix_sums[i - 1][j] + prefix_sums[i][j - 1] - \
                                    prefix_sums[i - 1][j - 1]

        # Helper function to calculate sum of subgrid
        def get_sum(r1, c1, r2, c2):
            return prefix_sums[r2][c2] - prefix_sums[r1 - 1][c2] - prefix_sums[r2][c1 - 1] + prefix_sums[r1 - 1][c1 - 1]

        # Initialize dp arrays
        dp1 = [float('inf')] * n
        dp2 = [float('inf')] * n
        dp3 = [float('inf')] * n

        # Compute dp1
        for j in range(n):
            for i in range(1, m - 1):
                dp1[j] = min(dp1[j], get_sum(1, 1, i + 1, j + 1))

        # Compute dp2
        for j in range(n):
            for i in range(1, m - 1):
                dp2[j] = min(dp2[j], dp1[i] + get_sum(i + 1, 1, m, j + 1))

        # Compute dp3
        for j in range(n):
            for i in range(1, m - 1):
                dp3[j] = min(dp3[j], dp2[i] + get_sum(i + 1, 1, m, j + 1))

        # Find minimum sum among dp3
        min_sum = min(dp3)

        return min_sum if min_sum != float('inf') else 0


grid = [[1, 0, 1, 0], [0, 1, 0, 1]]
sol = Solution()
print(sol.minimunSum(grid))


def minimumArea(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    rows_with_ones = [r for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1]
    cols_with_ones = [c for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1]

    if not rows_with_ones or not cols_with_ones:
        return 0

    min_row = min(rows_with_ones)
    max_row = max(rows_with_ones)
    min_col = min(cols_with_ones)
    max_col = max(cols_with_ones)

    width = max_col - min_col + 1
    height = max_row - min_row + 1

    area = width * height

    return area
