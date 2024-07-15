class Solution(object):
    def countOfAtoms(self, formula):
        import collections

        stack = [collections.defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                for elem in top:
                    stack[-1][elem] += top[elem] * multiplier
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][element] += count

        final_counts = stack.pop()

        result = ''
        for element in sorted(final_counts):
            result += element
            if final_counts[element] > 1:
                result += str(final_counts[element])

        return result


formula = "Mg(OH)2"
sol = Solution()
print(sol.countOfAtoms(formula))
