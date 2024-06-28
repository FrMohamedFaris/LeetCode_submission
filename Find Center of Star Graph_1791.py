class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]

edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
sol = Solution()
print(sol.findCenter(edges))
