class Solution(object):
    def equalSubstring(self, s, t, maxCost):

        start = 0
        c = 0
        max_length = 0

        for end in range(len(s)):

            c += abs(ord(s[end]) - ord(t[end]))

            while c <= maxCost:
                c -= abs(ord(s[end]) - ord(t[end]))
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length


s = "abcd"
t = "bcdf"
maxCost = 3

sol = Solution()

print(sol.equalSubstring(s, t, maxCost))
