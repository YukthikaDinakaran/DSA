# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None
        while l1 and l2:
            if (l1.val <= l2.val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
             cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
            
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        