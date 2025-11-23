
# ------------------------------------------------------------------------------------------------------------
# Problem no :  392
# Problem heading :  Is Subsequence
# Problem Link : https://leetcode.com/problems/is-subsequence/description/

# Problem Description : 
#   Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#   A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
#   without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "abc", t = "ahbgdc"
#   Output: true

#   Input: s = "axc", t = "ahbgdc"
#   Output: false

#   Explanation: 
#  "ace" is a subsequence of "abcde" while "aec" is not.
#  *******************************************************************


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp=list(t)
        for i in s:
            if(i in temp):
                k=temp.index(i)
                temp=temp[k+1:]
            else:
                return False
        return True    