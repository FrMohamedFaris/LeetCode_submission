import math


class Solution(object):
    def judgeSquareSum(self, c):

        if c < 0:
            return False

        a = 0
        b = int(math.sqrt(c))

        while a <= b:
            sum_of_squares = a * a + b * b
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                a += 1
            else:
                b -= 1

        return False


c = 4
sol = Solution()
print(sol.judgeSquareSum(c))
