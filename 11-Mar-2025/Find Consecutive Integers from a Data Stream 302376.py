# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count+= 1
            return self.count >= self.k
        self.count = 0
        return False


# Your DataStream obje/t will be instantiated and called as such:
# obj = DataStream(va-lopmue, k)
# param_1 = obj.consec(num)