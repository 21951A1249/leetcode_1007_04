class Solution:
    def deleteDuplicates(self, head):
        t=head
        if head is not None:
            while t.next is not None:
                if t.val==t.next.val:
                    t.next=t.next.next
                else:
                    t=t.next
        return head
    
