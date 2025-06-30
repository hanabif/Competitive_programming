# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.mergeTwo(list1,list2))
            lists = merged
        return lists[0]
                

    def mergeTwo(self, list1, list2):
        node = ListNode()
        instance = node
        
        while list1 and list2:
            if list1.val < list2.val:
                instance.next = list1
                list1 = list1.next
            else:
                instance.next = list2
                list2 = list2.next
            instance = instance.next
        
        if list1:
            instance.next = list1
        if list2:
            instance.next = list2
        
        return node.next