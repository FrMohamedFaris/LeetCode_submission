import heapq


class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        max_profit_heap = []
        current_index = 0

        for _ in range(k):

            while current_index < len(projects) and projects[current_index][0] <= w:
                heapq.heappush(max_profit_heap, -projects[current_index][1])
                current_index += 1

            if not max_profit_heap:
                break

            w += -heapq.heappop(max_profit_heap)

        return w


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
sol = Solution()
print(sol.findMaximizedCapital(k, w, profits, capital))
