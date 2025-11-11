class Solution(object):
    def sortList(self, head):
        if head is None:
            return None
        ptr=head
        arr=[]
        while ptr is not None:
            arr.append(ptr.val)
            ptr=ptr.next
        arr.sort()
        n = ListNode(arr[0])
        head=n
        temp=head
        for i in range(1,len(arr)):
            n1 = ListNode(arr[i])
            temp.next=n1
            temp=temp.next       
        return head