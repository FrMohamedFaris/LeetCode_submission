class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.component_count = size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.component_count -= 1
            return True
        return False

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)

        used_edges = 0

        for edge in edges:
            if edge[0] == 3:
                if alice_uf.union(edge[1] - 1, edge[2] - 1):
                    bob_uf.union(edge[1] - 1, edge[2] - 1)
                    used_edges += 1


        for edge in edges:
            if edge[0] == 1:
                if alice_uf.union(edge[1] - 1, edge[2] - 1):
                    used_edges += 1


        for edge in edges:
            if edge[0] == 2:
                if bob_uf.union(edge[1] - 1, edge[2] - 1):
                    used_edges += 1


        if alice_uf.component_count > 1 or bob_uf.component_count > 1:
            return -1

        return len(edges) - used_edges


n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
sol = Solution()
print(sol.maxNumEdgesToRemove(n, edges))
