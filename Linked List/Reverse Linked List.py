# ------------------------------------------------------------------------------------------------------------
# Problem no :  206
# Problem heading :  Reverse Linked List
# Problem Link : https://leetcode.com/problems/reverse-linked-list/description/

# Problem Description : 
#   Given the head of a singly linked list, reverse the list, and return the reversed list.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: head = [1,2,3,4,5]
#   Output: [5,4,3,2,1]
#   Explanation: we use the three pointer approach to reverse the linked list. Prev, current and Next
#   next = current.next
#   current.next = prev
#   prev = current
#   current = next
#   
#  *******************************************************************


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        next = None
        curr = head
        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head