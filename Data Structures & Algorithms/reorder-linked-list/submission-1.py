# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        originalHead = head
        secondHead = None
        while head:
            length += 1
            head = head.next
        count = 0
        head = originalHead
        while head:
            count += 1
            if count > math.floor(length / 2) - 1:
                secondHead = head.next
                head.next = None
                break
            else:
                head = head.next
        head = originalHead
        secondHead = self.reverseList(secondHead)
        node = dummy = ListNode()
        while head and secondHead:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = secondHead
            secondHead = secondHead.next
            dummy = dummy.next
        self.printList(node.next)
        head = node.next
        


    def reverseList(self, head: Optional[ListNode]):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next