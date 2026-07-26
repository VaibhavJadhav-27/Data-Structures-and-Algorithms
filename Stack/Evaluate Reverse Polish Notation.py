
# ------------------------------------------------------------------------------------------------------------
# Problem no :  150
# Problem heading :  Evaluate Reverse Polish Notation
# Problem Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# Problem Description : 
#   You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#   Evaluate the expression. Return an integer that represents the value of the expression.
#   Note that:
#   The valid operators are '+', '-', '*', and '/'.
#   Each operand may be an integer or another expression.
#   The division between two integers always truncates toward zero.
#   There will not be any division by zero.
#   The input represents a valid arithmetic expression in a reverse polish notation.
#   The answer and all the intermediate calculations can be represented in a 32-bit integer.

#  *******************************************************************
#   Input: tokens = ["2","1","+","3","*"]
#   Output: 9
#   Explanation:
#   ((2 + 1) * 3) = 9

#   Input: tokens = ["4","13","15","/","+"]
#   Output: 6
#   Explanation:
#   (4 + (13 / 5)) = 6

#  *******************************************************************


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(0,len(tokens)):
            if(tokens[i] not in ["+","-","*","/"]):
                stack.append(int(tokens[i]))
                continue
            right = stack.pop()
            left = stack.pop()
            if(tokens[i]=="+"):
                ans =  left +  right
            elif(tokens[i]=="-"):
                ans = left - right
            elif(tokens[i]=="*"):
                ans = left * right
            elif(tokens[i]=="/"):
                ans = int(float(left) / right)
            stack.append(ans)
        return stack[-1]