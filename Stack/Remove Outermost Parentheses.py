
# ------------------------------------------------------------------------------------------------------------
# Problem no :  1021
# Problem heading :  Remove Outermost Parentheses
# Problem Link : https://leetcode.com/problems/remove-outermost-parentheses/description/

# Problem Description : 
#   A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
#   For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#   A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
#   Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
#   Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.    


#  *******************************************************************
#   Input: s = "(()())(())"
#   Output: "(()())(())"
#   Explanation:
#   The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
#   After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

#   Input: s = "(()())(())(()(()))"
#   Output: "(()())(())"
#   Explanation:
#   The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
#   After removing outer parentheses of each part, this is "()()" + "()" + "()" = "()()()".

#  *******************************************************************


class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ""
        temp = ""
        for i in range(0,len(s)):
            if(s[i]=="("):
                stack.append(s[i])
                temp = temp + s[i]
            elif(stack and s[i]==")"):
                stack.pop()
                temp=temp + s[i]
            if(len(stack)==0):
                ans = ans  + temp[1:-1]
                temp = ""
        return ans
            