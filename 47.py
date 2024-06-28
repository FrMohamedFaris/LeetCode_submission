import heapq


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """

        n = len(tasks)
        indexed_task = [(tasks[i][0], tasks[i][1], i) for i in range(n)]

        indexed_task.sort()

        result = []
        min_heap = []
        time = 0
        i = 0

        while i < n or min_heap:

            while i < n and indexed_task[i][0] <= time:
                enqueue_time, processing_time, index = indexed_task[i]
                heapq.heappush(min_heap, (processing_time, index))
                i += 1

            if min_heap:

                processing_time, index = heapq.heappop(min_heap)
                time += processing_time
                result.append(index)
            else:

                if i < n:
                    time = indexed_task[i][0]
        return result


tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
sol = Solution()
print(sol.getOrder(tasks))
