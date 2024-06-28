class Solution(object):
    def countCompleteDayPairs1(self, hours):

        hours_dict = []
        n = len(hours)

        for i in range(n):
            for j in range(i + 1, n):
                if i < j:
                    complete_day = hours[i] + hours[j]
                    if complete_day % 24 == 0:
                        hours_dict.append((i, j))
        return len(hours_dict)

    def countCompleteDayPairs(self, hours):
        from collections import defaultdict

        remainder_counts = defaultdict(int)
        count_pairs = 0

        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            count_pairs += remainder_counts[complement]
            remainder_counts[remainder] += 1

        return count_pairs

    def maximumTotalDamage(self, power):
        from collections import defaultdict

        # Count the frequency of each spell damage
        count = defaultdict(int)
        for p in power:
            count[p] += 1

        # Sort unique spell damages
        unique_powers = sorted(count.keys())

        # Initialize DP array
        dp = [0] * (len(unique_powers) + 1)

        for i in range(len(unique_powers)):
            damage = unique_powers[i]
            freq = count[damage]

            # Maximum damage without taking the current spell
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Maximum damage with taking the current spell
            if i >= 1 and unique_powers[i] - unique_powers[i - 1] > 2:
                dp[i + 1] = max(dp[i + 1], dp[i - 1] + damage * freq)
            elif i >= 2 and unique_powers[i] - unique_powers[i - 2] > 2:
                dp[i + 1] = max(dp[i + 1], dp[i - 2] + damage * freq)
            else:
                dp[i + 1] = max(dp[i + 1], damage * freq)

        return max(dp)


hours = [12, 12, 30, 24, 24]
power = [7, 1, 6, 6]

sol = Solution()
print(sol.maximumTotalDamage(power))
