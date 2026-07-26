
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1544
# Problem heading :  Make The String Great
# Problem Link : https://leetcode.com/problems/make-the-string-great/description/

# Problem Description : 
#   Given a string s of lower and upper case English letters. 
#   A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

#   0 <= i <= s.length - 2
#   s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
#   To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
#   Return the string after making it good. The answer is guaranteed to be unique under the given constraints..


#  *******************************************************************
#   Input: s = "leEeetcode"
#   Output: "leEeetcode"
#   Explanation:
#   In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

#   Input: s = "abBAcC"
#   Output: "abc"
#   Explanation:
#   "abBAcC" -> "aAcC" -> "abc"

#  *******************************************************************
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if(stack and s[i].lower()!=stack[-1].lower()):
                stack.append(s[i])
            else:
                if(stack and ((s[i].islower() and stack[-1].isupper()) or (s[i].isupper() and stack[-1].islower()))):
                    stack.pop()
                else:
                    stack.append(s[i])
        return "".join(stack)
            
        