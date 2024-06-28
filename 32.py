class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        total_moves = 0
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
        return total_moves


seats = [3, 1, 5]
students = [2, 7, 4]
sol = Solution()
print(sol.minMovesToSeat(seats, students))
