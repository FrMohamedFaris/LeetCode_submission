class Solution(object):
    def reverse(self, n):

        reversed_num = 0

        is_negative = n < 0

        n = abs(n)

        while n != 0:

            last_digit = n % 10

            if (reversed_num > (2 ** 31 - 1) // 10 or
                    (reversed_num == (2 ** 31 - 1) // 10 and last_digit > 7)):
                return 0
            if (reversed_num > 2 ** 31 // 10 or
                    (reversed_num == 2 ** 31 // 10 and last_digit > 8)):
                return 0

            reversed_num = reversed_num * 10 + last_digit

            n //= 10

        if is_negative:
            reversed_num = -reversed_num

        if reversed_num < -2 ** 31 or reversed_num > 2 ** 31 - 1:
            return 0

        return reversed_num


x = 123
sol = Solution()
print(sol.reverse(x))

# count = sum(num >= i for num in nums
