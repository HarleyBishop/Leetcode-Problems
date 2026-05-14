




# NOTES: Simple solution when thought out. Use 3 values 1 to track current postion 1 to track the previous value and one to track what the next value is. While head so while there is a next node set the future value before chain is broken. 
# Then set the next vvalue of the current head to the previous node so reverse the link. Then move the previous pointer to where the head is and move the head forward. You return previous as it is holding the final node pointing at the second last value while the head is None as it is moved forward.






# ! Solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


