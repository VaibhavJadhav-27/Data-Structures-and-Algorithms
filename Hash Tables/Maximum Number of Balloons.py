# ------------------------------------------------------------------------------------------------------------
# Problem no :  1189
# Problem heading :  Maximum Number of Balloons
# Problem Link : https://leetcode.com/problems/maximum-number-of-balloons/

# Problem Description :
#   Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#   You can use each character in text at most once. Each character can only be used once.
#   Return the maximum number of instances that can be formed.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input: text = "nlaebolko"
#   Output: 1
#
#   Example 2:
#   Input: text = "loonbalxballpoon"
#   Output: 2
#
#   Example 3:
#   Input: text = "leetcode"
#   Output: 0
#  *******************************************************************

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        string = "balloon"
        temp =[]
        if(len(text)<7):
            return 0
        for i in string:
            temp.append(text.count(i))
        temp[2] = temp[2]//2
        temp[5] = temp[5]//2
        return min(temp)
