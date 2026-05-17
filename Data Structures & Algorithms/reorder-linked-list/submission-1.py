# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.vaError, l = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        fast,slow = head,head

        while slow and slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev,curr = None,slow.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        slow.next = None

        A,B = head,prev

        while A and B:
            ANext = A.next
            BNext = B.next
            A.next = B
            if not ANext:
                break
            B.next = ANext
            A = ANext
            B = BNext

        return