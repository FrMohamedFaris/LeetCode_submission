class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sorted_l1 = l1[::-1]
        sorted_l2 = l2[::-1]

        combined_l1 = int(''.join(map(str, sorted_l1)))
        combined_l2 = int(''.join(map(str, sorted_l2)))

        output = combined_l1 + combined_l2

        output = [int(char) for char in list(str(output))]

        return output


list1 = [2, 4, 3]
list2 = [5, 6, 4]
sol = Solution()
print(sol.addTwoNumbers(list1, list2))
