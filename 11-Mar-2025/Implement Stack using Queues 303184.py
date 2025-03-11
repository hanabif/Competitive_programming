# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.deq = deque()

    def push(self, x: int) -> None:
        self.deq.append(x)

    def pop(self) -> int:
        for i in range(len(self.deq) - 1):
            self.deq.append(self.deq.popleft())
        return self.deq.popleft()

    def top(self) -> int:
        return self.deq[-1]

    def empty(self) -> bool:
        if self.deq:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()