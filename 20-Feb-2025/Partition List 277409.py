# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: 
            return 
        arr=[]
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        less = Counter(num for num in arr if num < x)     
        
        newhead = ListNode(arr[0]) 
        traverse = newhead 
        for num in arr:
            if num in less and less[num] > 0:
                traverse.next = ListNode(num)
                traverse = traverse.next
                less[num]-=1
        for num in arr:
            if num not in less :
                traverse.next = ListNode(num)
                traverse = traverse.next   
        return newhead.next
                

            

        
        
        