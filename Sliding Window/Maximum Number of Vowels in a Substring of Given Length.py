
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1456
# Problem heading :  Maximum Number of Vowels in a Substring of Given Length
# Problem Link : https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

# Problem Description : 
#   Given a string and an integer k, return the maximum number of vowel letters in any substring of s with length k.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "abciiidef", k = 3
#   Output: 3
#   Explanation: The substring "iii" contains 3 vowel letters.

#   Input: s = "aeiou", k = 2
#   Output: 2
#   Explanation: Any substring of length 2 contains 2 vowel letters.
#  *******************************************************************
#   Explanation: The substring "aei" has the maximum number of vowels.
#  *******************************************************************


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a","e","i","o","u"]
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count=count+1
        left = 0
        max_count=count
        for right in range(k, len(s)):
            if(s[left] in vowels):
                count =  count - 1
            if(s[right] in vowels):
                count = count + 1
            left = left + 1
        
            max_count = max(max_count, count)
        
        return max_count

        