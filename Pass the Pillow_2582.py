class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current_postion = 1
        direction = 1
        for _ in range(time):
            if current_postion == 1:
                direction = 1
            elif current_postion == n:
                direction = -1
            current_postion += direction
        return current_postion


n = 4
time = 5
sol = Solution()
print(sol.passThePillow(n, time))
