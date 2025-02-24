# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self, key , val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # maps key to value

        #dummy nodes to tell us which one is least recently(left) and most recently used(right)
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next , self.right.prev = self.right , self.left
    #remove from list
    def remove(self, ListNode):
        prev, nxt = ListNode.prev, ListNode.next
        prev.next, nxt.prev = nxt, prev

    #insert at right
    def insert(self , ListNode):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = ListNode
        ListNode.next, ListNode.prev = nxt, prev
          

    
    def get(self, key: int) -> int:
        if key in self.cache:
           self.remove(self.cache[key])
           self.insert(self.cache[key])
           return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key , value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from list and delete LRU from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)