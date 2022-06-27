# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # two pointers fast - slow - Floyd cycle detection
        fast = head
        slow = head
        prev = None # previous node 
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        while prev:
            if head.val != prev.val: return False
            head, prev = head.next, prev.next
        return True