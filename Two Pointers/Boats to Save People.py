# ------------------------------------------------------------------------------------------------------------
# Problem no :  881
# Problem heading :  Boats to Save People
# Problem Link : https://leetcode.com/problems/boats-to-save-people/description/

# Problem Description :
#   You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat can carry at most two people at the same time, provided the sum of the weight of those people is at most limit.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input:  people = [1,2], limit = 3
#   Output: 1
#   Explanation: 1 boat (1, 2) saves all people.
#
#   Example 2:
#   Input:  people = [3,2,2,1], limit = 3
#   Output: 3
#   Explanation: 3 boats (1, 2), (2) and (3) saves all people.
#  *******************************************************************


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        number_of_boats=0
        temp=sorted(people)
        i=0
        j=len(people)-1
        while(i<=j):
            if(temp[i]+temp[j]<=limit):
                number_of_boats=number_of_boats+1
                i=i+1
                j=j-1
            else:
                number_of_boats=number_of_boats+1
                j=j-1
        return number_of_boats

        