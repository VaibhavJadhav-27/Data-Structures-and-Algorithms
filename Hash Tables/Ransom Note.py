# ------------------------------------------------------------------------------------------------------------
# Problem no :  383
# Problem heading :  Ransom Note
# Problem Link : https://leetcode.com/problems/ransom-note/description/

# Problem Description :
#   Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#   Each letter in magazine can only be used once in ransomNote.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input: ransomNote = "a", magazine = "b"
#   Output: false
#
#   Example 2:
#   Input: ransomNote = "aa", magazine = "ab"
#   Output: false
#
#   Example 3:
#   Input: ransomNote = "aa", magazine = "aab"
#   Output: true
#
#   Explanation: We can construct "aa" from "aab" by using two 'a's and one 'b'.
#  *******************************************************************

# Initial Approach
# Time Complexity : O(n*m) where n is length of ransomNote and m is length of magazine
# Space Complexity : O(1)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        temp=magazine
        for i in ransomNote:
            if i not in temp:
                return False
            else:
                temp = temp.replace(i,"",1)
        return True
    

# Alternative Approach using Hash Map
# Time Complexity : O(n + m) where n is length of ransomNote and m is length of magazine
# Space Complexity : O(1)
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True