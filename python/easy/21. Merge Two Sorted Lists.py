# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative solution, we first pick our root Node and then compare 
        each current node from list1 & list2 to pick the next node
        
        time: O(n + m) ... where n = len(list1) & m = len(list2)
        space: O(1)
        """

        root = None

        if (list1 and not list2) or (list1 and list1.val < list2.val):
            root = list1
            list1 = list1.next
        elif list2:
            root = list2
            list2 = list2.next

        curr = root

        while(list1 and list2):
            if (list1.val < list2.val):
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        # if either lists aren't empty, append the end of the list to curr
        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2

        return root
            