class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        index = 0
        step = 1

        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(rows)


s = "PAYPALISHIRING"
numRows = 3
sol = Solution()
print(sol.convert(s, numRows))
