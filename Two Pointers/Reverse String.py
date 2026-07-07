# ------------------------------------------------------------------------------------------------------------
# Problem no :  344
# Problem heading :  Reverse String
# Problem Link : https://leetcode.com/problems/reverse-string/description/

# Problem Description :
#   Write a function that reverses a string. The input string is given as an array of characters s.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input:  s = ["h","e","l","l","o"]
#   Output: ["o","l","l","e","h"]
#   Explanation: The string "hello" is reversed to "olleh".
#
#   Example 2:
#   Input:  s = ["H","a","n","n","a","h"]
#   Output: ["h","a","n","n","a","H"]
#   Explanation: The string "hannah" is reversed to "hannah".
#  *******************************************************************

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while(i<j):
            s[i],s[j] = s[j] ,s[i]
            i=i+1
            j=j-1
        