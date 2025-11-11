# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        lst=[]
        while temp:
            lst.append(temp.val)
            temp=temp=temp.next

        lst.sort()
        temp=head
        for i in lst:
            temp.val=i
            temp=temp.next

        return head    