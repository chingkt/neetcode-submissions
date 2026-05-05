# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False