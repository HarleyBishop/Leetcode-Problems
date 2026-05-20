

#! Self made solution 

# * If you count the number of nodes ad N and u have n the nth node frome the end. You can do N - n = how many nodes forwards the nth node from the end is

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        # Count Nodes
        # N - n should equal the index of the node to remove from the start
        # e.g. n = 3 remove node 3 from from the start node e.g. node 4
        # [1, 2, 3, 4, 5, 6] = remove node 4. 6 - 3 = 3. So node is 3 from the start
        
        N = 0
        cur = head

        while cur:
            N += 1
            cur = cur.next
        
        T = N - n

        if T == 0:
            return head.next

        cur = head

        for i in range(T - 1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head


        


        

        