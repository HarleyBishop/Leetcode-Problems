

# ! Solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 2 pointers. 1 poiunter will move 2 times the speed of the other if they ever meet there is a cycle

        slow = head
        fast = head

        # Ensure the node exists so u dont try to access node.next on a non existent node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False


