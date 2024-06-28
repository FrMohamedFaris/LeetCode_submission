class Solution:
    def countPeaks(self, nums, queries):
        n = len(nums)
        peaks = [0] * n

        # Calculate initial peaks
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                peaks[i] = 1

        # Process queries
        results = []
        for query in queries:
            if query[0] == 1:  # Count peaks in range [li, ri]
                li, ri = query[1], query[2]
                count = sum(peaks[li + 1:ri])  # Only count peaks inside [li+1, ri-1]
                results.append(count)
            elif query[0] == 2:  # Update nums[indexi] = vali
                indexi, vali = query[1], query[2]
                current_value = nums[indexi]
                if current_value != vali:
                    nums[indexi] = vali
                    # Update peak status around indexi
                    if indexi > 1 and indexi < n - 1:
                        peaks[indexi - 1] = 1 if nums[indexi - 2] < vali > nums[indexi - 1] else 0
                        peaks[indexi] = 1 if nums[indexi - 1] < vali > nums[indexi + 1] else 0
                    results.append(0)  # Since it doesn't change the peak count directly

        return results


nums = [3,1,4,2,5]
queries = [[2,3,4],[1,0,4]]
sol = Solution()
print(sol.countPeaks(nums, queries))
