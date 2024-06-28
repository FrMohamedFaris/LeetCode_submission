class Solution(object):
    def scoreOfString(self, s):
        diff = 0
        for i in range(len(s)-1):
            next_val = (i + 1) % len(s)
            diff += abs(ord(s[i]) - ord(s[next_val]))
        return diff


s = "zaz"
sol = Solution()
print(sol.scoreOfString(s))
