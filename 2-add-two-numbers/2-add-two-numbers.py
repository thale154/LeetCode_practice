# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result 
        sum = 0
        while (l1 or l2 or sum):
            if (l1):
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            current.next = ListNode(sum%10)
            current = current.next
            
            sum = sum // 10
        
        return result.next