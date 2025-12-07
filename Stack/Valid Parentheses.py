
# ------------------------------------------------------------------------------------------------------------
# Problem no :  20
# Problem heading :  Valid Parentheses
# Problem Link : https://leetcode.com/problems/valid-parentheses/description/

# Problem Description : 
#   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#   An input string is valid if:

#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.

 

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "()[]{}"
#   Output: true

#   Input: s = "([)]"
#   Output: false

#  Explanation:
#   Using Stack data structure to keep track of opening brackets.
#   When encountering a closing bracket, check if it matches the top of the stack.
#  *******************************************************************


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack = []
        # pointer = -1
        # if(len(s)%2 !=0):
        #     return False
        # for i in s:
        #     if(i in ('(', '{','[')):
        #         stack.append(i)
        #         pointer=pointer +1
        #         print(pointer)
        #     elif(i in (')', '}',']') and pointer ==-1):
        #         return False
        #     elif(i==')' and stack[pointer]!='('):
        #         return False
        #     elif(i=='}' and stack[pointer]!='{'):
        #         return False
        #     elif(i==']' and stack[pointer]!='['):
        #         return False
        #     elif(i==')' and stack[pointer]=='('):
        #         stack.pop()
        #         pointer=pointer - 1
        #     elif(i=='}' and stack[pointer]=='{'):
        #         stack.pop()
        #         pointer=pointer - 1
        #     elif(i==']' and stack[pointer]=='['):
        #         stack.pop()
        #         pointer=pointer - 1
        # if(len(stack)>0):
        #     return False
        # else:
        #     return True

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs.values():           # opening
                stack.append(ch)
            elif ch in pairs:                  # closing
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # ignore any other characters or return False if invalid input
                return False

        return len(stack) == 0
        
    