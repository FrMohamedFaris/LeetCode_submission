
class Solution(object):
    def checkRecord(self,n):
        MOD = 10 ** 9 + 7

        # Initialize counts for records ending with 'P', 'L', 'A'
        end_with_P = [1, 0, 0]
        end_with_L = [0, 0, 0]
        end_with_A = [0, 0, 0]

        for i in range(1, n + 1):
            # Update counts for records ending with 'P'
            new_end_with_P = [
                (end_with_P[0] + end_with_L[0] + end_with_A[0]) % MOD,
                end_with_P[0],
                end_with_P[1]
            ]

            # Update counts for records ending with 'L'
            new_end_with_L = [
                (end_with_P[0] + end_with_L[0] + end_with_A[0] +
                 end_with_P[1] + end_with_A[1]) % MOD,
                end_with_L[0],
                end_with_L[1]
            ]

            # Update counts for records ending with 'A'
            new_end_with_A = [
                (end_with_P[0] + end_with_L[0] + end_with_A[0] +
                 end_with_P[1] + end_with_L[1] + end_with_A[1]) % MOD,
                end_with_A[0],
                end_with_A[1]
            ]

            end_with_P = new_end_with_P
            end_with_L = new_end_with_L
            end_with_A = new_end_with_A

        # Total count of valid records
        total_count = sum(end_with_P) + sum(end_with_L) + sum(end_with_A)
        return total_count % MOD



sol = Solution()
n =2
print(sol.checkRecord(n))