class Solution(object):
    def maximumGain(self, s, x, y):

        score = 0
        n = len(s)
        i = 0

        while i < n - 1:
            if s[i:i + 2] == "ab":
                score += x
                i += 2
            elif s[i:i + 2] == "ba":
                score += y
                i += 2
            else:
                i += 1

        return score


s = "aabbaaxybbaabb"
x = 5
y = 4
sol = Solution()
print(sol.maximumGain(s, x, y))
