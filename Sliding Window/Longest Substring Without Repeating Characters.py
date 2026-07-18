
# ------------------------------------------------------------------------------------------------------------
# Problem no :  3
# Problem heading :  Longest Substring Without Repeating Characters
# Problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Problem Description : 
#   Given a string s, find the length of the longest substring without repeating characters.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "abcabcbb"
#   Output: 3
#
#   Explanation: The answer is "abc", with the length of 3.

#
#  *******************************************************************

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        set1= set()
        longest_substring = 0
        for right in range(len(s)):
            if(s[right] not in set1):
                set1.add(s[right])
            
            else:
                while(s[right] in set1):
                    set1.discard(s[left])
                    left =  left + 1
                set1.add(s[right])
            
            longest_substring =  max(longest_substring, right - left + 1)
        return longest_substring