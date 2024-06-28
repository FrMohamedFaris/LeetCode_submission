class Solution(object):
    def intToRoman(self, num):
        val = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman_numerals = ""

        for (value, romans) in val:
            while num >= romans:
                roman_numerals = value
                num -= romans
        return roman_numerals


num = "III"
sol = Solution()
print(sol.intToRoman(num))
