
# * Due to the condifiton check while second_list.next it is unnecessary however remember that in other problems u may have to cut off the connection from the first and seconf half of the split list. e.g. the final node of the first half still points to the first value of the second half when split. Do this with a prev tracker

#! Solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Find Middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # Prev whill be the new final node or first node of 2nd half

        first_list, second_list = head, prev
        # Second list will be same or longer so guranteed to be final node
        while second_list.next:
            # Store the original next values of the list
            tmp1 = first_list.next
            tmp2 = second_list.next

            # Rearrange the node order
            first_list.next = second_list
            second_list.next = tmp1

            # Move to the next value in each list
            first_list = tmp1
            second_list = tmp2


    
        
    
            
            

        
        
    