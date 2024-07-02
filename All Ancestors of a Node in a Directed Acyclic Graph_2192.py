from collections import defaultdict


class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        ancestors = [set() for _ in range(n)]
        visited = [False] * n

        def dfs(node):
            if visited[node]:
                return ancestors[node]
            visited[node] = True
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            return ancestors[node]

        for i in range(n):
            dfs(i)

        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        return result


n = 8
edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
sol = Solution()
print(sol.getAncestors(n, edgeList))
