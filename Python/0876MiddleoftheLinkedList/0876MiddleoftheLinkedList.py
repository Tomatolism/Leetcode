# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        step1 = step2 = head

        while True:
            if not step2.next:
                return step1

            step2 = step2.next
            step1 = step1.next

            if not step2.next:
                return step1
            
            step2 = step2.next
