class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = '#'.join(f'^{s}$')
        n = len(t)
        p = [0] * n
        center = right = 0

        for i in range(1, n - 1):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])

            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > right:
                center, right = i, i + p[i]

        max_len, center_index = max((n, i) for i, n in enumerate(p))

        start = (center_index - max_len) // 2
        return s[start: start + max_len]


s = "cbbd"
sol = Solution()
print(sol.longestPalindrome(s))
