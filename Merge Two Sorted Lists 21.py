




# * NOTES: list1 and list2 are the lists head nodes so treat thjem as single nodes not a full list. Use a current node to track position and a dummy to be the head. Dummy is a node and cur is a pointer to a node. Key distinction

# ! Solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        head = ListNode()

        cur = head # Pointer to dummy's node

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1 #The current nexst position is the smaller value
                list1 = list1.next # Make the list1 start from the next node
                cur = cur.next # MOve to the next point
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return head.next