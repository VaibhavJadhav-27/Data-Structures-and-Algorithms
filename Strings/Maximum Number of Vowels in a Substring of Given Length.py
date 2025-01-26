
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1456
# Problem heading :  Maximum Number of Vowels in a Substring of Given Length
# Problem Link : https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

# Problem Description : 
#   Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#   Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "abciiidef", k = 3
#   Output: 3
#   Explanation: The substring "iii" contains 3 vowel letters.
#
#  *******************************************************************

class Solution:
    def maxVowels(self, s, k):
        #Use a set for a faster lookup
        vowels = {'a', 'e', 'i', 'o', 'u'} 
        res = 0
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        res = count

        # Slide the window by starting from index k
        for i in range(k, len(s)):
            if s[i - k] in vowels:  # Remove the vowel going out of the window
                count -= 1
            if s[i] in vowels:  # Add the vowel coming into the window
                count += 1

            res = max(res, count)
        
        return res