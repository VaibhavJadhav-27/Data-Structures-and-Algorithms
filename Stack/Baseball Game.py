
# ------------------------------------------------------------------------------------------------------------
# Problem no :  682
# Problem heading :  Baseball Game
# Problem Link : https://leetcode.com/problems/baseball-game/description/

# Problem Description : 
#   You are keeping score for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

#   You are given a list of strings operations, where each string represents an operation. The operations can be:

#   1. An integer x: Record a new score of x.
#   2. '+': Record a new score that is the sum of the previous two scores.
#   3. 'D': Record a new score that is the double of the previous score.
#   4. 'C': Invalidate the previous score, removing it from the record.

#   Return the sum of all the scores on the record after applying all the operations.

#  *******************************************************************
#   Input: ["5", "2", "C", "D", "+"]
#   Output: 30
#   Explanation:
#   "5" - Add 5 to the record, record is now [5].
#   "2" - Add 2 to the record, record is now [5, 2].
#   "C" - Invalidate and remove the previous score, record is now [5].
#   "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
#   "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
#  The total sum is 5 + 10 + 15 = 30.

#   Input: ["5", "-2", "4", "C", "D", "9", "+", "+"]
#   Output: 28
#  Explanation:
#   "5" - Add 5 to the record, record is now [5].
#   "-2" - Add -2 to the record, record is now [5, -2].
#   "4" - Add 4 to the record, record is now [5, -2, 4].
#   "C" - Invalidate and remove the previous score, record is now [5, -2].
#   "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
#   "9" - Add 9 to the record, record is now [5, -2, -4, 9].
#   "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
#   "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
#  The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 28.
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
