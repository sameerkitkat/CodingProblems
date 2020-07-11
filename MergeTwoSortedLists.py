 def mergeTwoLists(l1, l2):

        dummy = ListNode(-1)
        pointer = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next

        if l1 is None:
            pointer.next = l2
        if l2 is None:
            pointer.next = l1

        return dummy.next
