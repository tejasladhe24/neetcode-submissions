# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        A,B = list1,list2

        newHead = ListNode()
        temp = newHead

        while A and B:
            if A.val < B.val:
                temp.next = A
                A = A.next
            else:
                temp.next = B
                B = B.next

            temp = temp.next

        temp.next = A or B

        return newHead.next