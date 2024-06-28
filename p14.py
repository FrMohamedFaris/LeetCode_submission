class Solution(object):
    def findRelativeRanks(self, score):

        sorted_s = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        print(sorted_s)

        result = [''] * len(score)

        for rank, (index, scores) in enumerate(sorted_s):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)


        return result


score = [5, 4, 3, 2, 1]
sol = Solution()
print(sol.findRelativeRanks(score))
