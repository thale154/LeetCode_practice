# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # two pointers fast - slow - Floyd cycle detection
        fast = slow = head
        prev = None # previous node 
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev = None
        while slow:
            #tmp = slow.next
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True