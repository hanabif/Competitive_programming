# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
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
        # Returning the node next because the init value is set to zero.
        return node.next