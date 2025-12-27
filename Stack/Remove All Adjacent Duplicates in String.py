# ------------------------------------------------------------------------------------------------------------
# Problem no :  1047
# Problem heading :  Remove All Adjacent Duplicates in String
# Problem Link : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

# Problem Description :
#   You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
#   We repeatedly make duplicate removals on s until we can no longer do so.
#   Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input: s = "abbaca"
#   Output: "ca"
#   Explanation: "abbaca" -> "aaca" -> "ca"
#
#   Example 2:
#   Input: s = "azxxzy"
#   Output: "ay"
#   Explanation: "azxxzy" -> "azzy" -> "ay"
#  *******************************************************************

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s)<1):
            return ""
        stack = []
        stack.append(s[0])
        p =0
        if len(s)==1:
            return s
        for i in range(1,len(s)):
            if(p>=0 and s[i] == stack[p]):
                stack.pop()
                p=p-1
            elif(p<0):
                stack.append(s[i])
                p=p+1
            elif(p>=0 and s[i] != stack[p]):
                stack.append(s[i])
                p=p+1
        return "".join(stack)
