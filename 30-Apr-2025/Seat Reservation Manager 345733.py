# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.unreserved = []
        for i in range(1,self.n):
            self.unreserved.append(i)
        heapq.heapify(self.unreserved)

    def reserve(self) -> int:
        if self.unreserved:
            return heapq.heappop(self.unreserved)
        return self.n

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved,seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)