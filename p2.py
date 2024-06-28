import itertools


class Solution(object):
    def getPermutation(self, n, k):
        l = list(range(1, n + 1))

        permuation_list = list(itertools.permutations(l))
        permutations_str = [''.join(map(str, perm)) for perm in permuation_list]

        return permutations_str[k-1]


n = 4
sol = Solution()
print(sol.getPermutation(n, k=9))
