# ------------------------------------------------------------------------------------------------------------
# Problem no :  234
# Problem heading :  Palindrome Linked List
# Problem Link : https://leetcode.com/problems/palindrome-linked-list/description/

# Problem Description :
#   Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input: head = [1,2,2,1]
#   Output: true
#
#   Example 2:
#   Input: head = [1,2]
#   Output: false
#  *******************************************************************

## Approach :
# 1. Use the fast and slow pointer technique to find the middle of the linked list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Find the middle of the linked list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        prev = None
        curr = slow.next
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Compare the first half and the reversed second half
        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True


# Time Complexity: O(n)
# Space Complexity: O(1)  


# ------------------------------------------------------------------------------------------------------------
# Approach 2 :

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        temp=[]
        while(head.next!=None):
            temp.append(head.val)
            head= head.next
        temp.append(head.val)
        reversetemp=temp[::-1]
        if(temp==reversetemp):
            return True
        else:
            return False
        
# Time Complexity: O(n)
# Space Complexity: O(n)