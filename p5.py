class Solution(object):
    def checkRecord(self, n):
        MOD = 10 ** 9 + 7

        count_P = 1
        count_PL = 1
        count_LL = 0
        count_A = 1
        count_AL = 0
        count_ALL = 0

        for length in range(2, n + 1):
            new_count_P = (count_P + count_PL + count_LL) % MOD
            new_count_PL = count_P
            new_count_LL = count_PL
            new_count_A = (count_P + count_PL + count_LL + count_A + count_AL + count_ALL) % MOD
            new_count_AL = count_A
            new_count_ALL = count_AL

            count_P, count_PL, count_LL, count_A, count_AL, count_ALL = new_count_P, new_count_PL, new_count_LL, new_count_A, new_count_AL, new_count_ALL

        total = (count_P + count_PL + count_LL + count_A + count_AL + count_ALL) % MOD
        return total

    def addTwoNumbers(self,l1, l2):
        carry = 0
        result = []

        # Iterate over both lists simultaneously
        for i in range(max(len(l1), len(l2))):
            # Get the digits from the lists or 0 if out of bounds
            digit1 = l1[i] if i < len(l1) else 0
            digit2 = l2[i] if i < len(l2) else 0

            # Add the digits and the carry
            total = digit1 + digit2 + carry

            # Update the carry and append the result
            carry = total // 10
            result.append(total % 10)

        # If there's still a carry after the loop, append it
        if carry:
            result.append(carry)

        return result

list1 = [2, 4, 3]
list2 = [5, 6, 7]

n = 2
sol = Solution()
print(sol.addTwoNumbers(list1, list2))
