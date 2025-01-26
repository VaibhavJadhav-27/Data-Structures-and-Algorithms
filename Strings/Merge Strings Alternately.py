
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1768
# Problem heading :  Merge Strings Alternately
# Problem Link : https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

# Problem Description : 
#   You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
#   If a string is longer than the other, append the additional letters onto the end of the merged string. 
#   Return the merged string.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: word1 = "ab", word2 = "pqrs"
#   Output: "apbqrs"
#   Explanation: Notice that as word2 is longer, "rs" is appended to the end.

#   word1:  a   b 
#   word2:    p   q   r   s
#   merged: a p b q   r   s
#
#  *******************************************************************


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=""
        min_length_str = min(len(word1),len(word2))
        for i in range(0,min_length_str):
            result  = result + word1[i] + word2[i]
        result = result + word1[min_length_str:] + word2[min_length_str:]
        return result
        