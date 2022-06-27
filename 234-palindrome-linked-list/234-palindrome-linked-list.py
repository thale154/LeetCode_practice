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
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        prev = None # previous node 
        while slow != None:
            #tmp = slow.next
            slow.next, prev, slow = prev, slow, slow.next
        while prev:
            if head.val != prev.val: return False
            head = head.next
            prev = prev.next
        return True