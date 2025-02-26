# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class List:
    def __init__(self, x, next=None, prev=None):
        self.val = x
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.tail = List(homepage)

    def visit(self, url: str) -> None:
        newNode = List(url)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode   

    def back(self, steps: int) -> str:
        curr = self.tail

        while curr and steps:
            steps-=1
            curr = curr.prev
        
        self.tail = curr
        if curr:
            return self.tail.val
        else:
            self.tail = self.head
            return self.tail.val

    def forward(self, steps: int) -> str:
        curr = self.tail
        while curr.next and steps:
            steps-=1
            curr = curr.next
        
        self.tail = curr
        return self.tail.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)