class Solution(object):
    def appendCharacters(self, s, t):

        s_len, t_len = len(s), len(t)

        t_index = 0

        for char in s:
            if t_index < t_len and char == t[t_index]:
                t_index += 1

        remaining_char = t_len - t_index

        return remaining_char


s = "coaching"
t = "coding"
sol = Solution()
print(sol.appendCharacters(s, t))
