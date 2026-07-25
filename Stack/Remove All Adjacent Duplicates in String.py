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
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        add = 0
        for i in operations:
            if(i not in ["+","C","D"]):
                stack.append(int(i))
                add = add + int(i)
                
            elif(i=="+"):
                sum_of_two_scores = stack[-1] + stack[-2]
                add = add + sum_of_two_scores
                stack.append(sum_of_two_scores)

            elif(i=="D"):
                add = add + (stack[-1]*2)
                stack.append((stack[-1]*2))

            elif(i=="C"):
                add = add - stack[-1]
                stack.pop()
        return add
