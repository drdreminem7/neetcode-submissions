# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverseList(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next

            return prev

        second_half = slow.next
        slow.next = None
        second_half = reverseList(second_half)

        iter = head
        while second_half:
            second_half_temp, iter_temp = second_half.next, iter.next
            iter.next = second_half
            second_half.next = iter_temp
            iter = iter_temp
            second_half = second_half_temp
