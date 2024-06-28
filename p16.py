class Solution(object):
    def numSteps(self, s):

        s = int(s, 2)
        obtain = 0
        while s > 1:
            if s % 2 == 0:
                s = s // 2

            else:
                s += 1

            obtain += 1

        return obtain


s = "11000"
sol = Solution()
print(sol.numSteps(s))
