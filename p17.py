class Solution(object):
    def numSteps(self, s):
        obtain = 0
        carry = 0


        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:

                carry = 1
                obtain += 2
            else:
                obtain += 1


        return obtain + carry


s = "1101"
sol = Solution()
print(sol.numSteps(s))