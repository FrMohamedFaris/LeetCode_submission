import re


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = []

        for i in s:
            if i == ")":
                temp = []
                while sl and sl[-1] != "(":
                    temp.append(sl.pop())
                if sl and sl[-1] == "(":
                    sl.pop()
                sl.extend(temp)
            else:
                sl.append(i)
        return "".join(sl)


s = "(u(love)i)"
sol = Solution()
print(sol.reverseParentheses(s))
