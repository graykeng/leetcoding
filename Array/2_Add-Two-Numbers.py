# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = ListNode()
        current = ret
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = val1 + val2 + carry
            carry = temp // 10
            temp = temp % 10
            current.val = temp
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                current.next = ListNode()
                current = current.next
        return ret