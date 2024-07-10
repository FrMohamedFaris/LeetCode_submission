class Solution(object):
    def minOperations(self, logs):
        s = []
        for log in logs:
            if log == "./":
                continue

            elif log == "../":
                if s:
                    s.pop()
            else:
                s.append(log)
        return len(s)


logs = ["d1/", "d2/", "../", "d21/", "./"]
sol = Solution()
print(sol.minOperations(logs))
