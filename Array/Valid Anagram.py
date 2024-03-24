# ------------------------------------------------------------------------------------------------------------
# Problem no :  242
# Problem heading :  Valid Anagram
# Problem Link : https://leetcode.com/problems/valid-anagram/description/

# Problem Description : 
#   Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#   An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "anagram", t = "nagaram"
#   Output: true
#   Explanation: Your function should return True when the count of each  unique letter in the string matches the count of each letter in another string
#   
#  *******************************************************************

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!= len(t)):
            return False
        set_s =  set(s)
        for i in set_s:
            if(s.count(i)!=t.count(i)):
                return False
        return True

        