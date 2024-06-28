class Solution(object):
    def maxDistance(self, position, m):

        position.sort()

        low, high = 1, position[-1]

        while low <= high:
            mid = (low + high) // 2
            count = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        break

            if count >= m:

                
                low = mid + 1
            else:
                high = mid - 1

        return high


position = [1, 2, 3, 4, 7]
m = 3
sol = Solution()
print(sol.maxDistance(position, m))
