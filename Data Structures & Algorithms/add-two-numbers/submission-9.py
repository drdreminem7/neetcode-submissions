# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        trailing_sum = 0
        while l1 or l2 or trailing_sum:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val

            summ = l1_val + l2_val + trailing_sum
            trailing_sum = summ // 10
            digit = summ % 10

            curr.next = ListNode(digit)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

