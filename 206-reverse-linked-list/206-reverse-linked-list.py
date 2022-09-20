# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
''' Iterative methode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while(cur):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
'''    
#Recursion method
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head or not head.next):
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return rest