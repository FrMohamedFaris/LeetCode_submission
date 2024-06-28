class Solution(object):
    def isMatch(self, s, p):
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = -1
        match = 0

        while s_idx < s_len:
            if p_idx < p_len and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                match = s_idx
                p_idx += 1
            elif star_idx != -1:
                p_idx = star_idx + 1
                match += 1
                s_idx = match
            else:
                return False

        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1

        return p_idx == p_len


s = "aa"
p = "*"
sol = Solution()
print(sol.isMatch(s, p))
