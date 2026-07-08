# ------------------------------------------------------------------------------------------------------------
# Problem no :  202
# Problem heading :  Happy Number
# Problem Link : https://leetcode.com/problems/happy-number/

# Problem Description :
#   Write an algorithm to determine if a number n is happy.
#   A happy number is a number defined by the following process:
#   Starting with any positive integer, replace the number by the sum of the squares of its digits.
#   Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#   Those numbers for which this process ends in 1 are happy numbers.
#   Return true if n is a happy number, false otherwise.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input: n = 19
#   Output: true
#   Explanation:
#   1^2 + 9^2 = 82
#   8^2 + 2^2 = 68
#   6^2 + 8^2 = 100
#   1^2 + 0^2 + 0^2 = 1
#
#   Example 2:
#   Input: n = 2
#   Output: false
#
#   Example 3:
#   Input: n = 1
#   Output: true
#  *******************************************************************

class Solution(object):
    def next_number(self,n):
        total=0
        while n>0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited=set()
        while n!=1:
            if n in visited:
                return False
            visited.add(n)
            n=self.next_number(n)
        return True
        
        