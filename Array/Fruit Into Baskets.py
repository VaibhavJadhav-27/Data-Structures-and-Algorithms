
# ------------------------------------------------------------------------------------------------------------
# Problem no :  904
# Problem heading :  Fruit Into Baskets
# Problem Link : https://leetcode.com/problems/fruits-into-baskets/description/

# Problem Description : 
#   You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

#   You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

#   You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
#   Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
#   Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

#   Given the integer array fruits, return the maximum number of fruits you can pick.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: fruits = [1,2,1]
#   Output: 3
#
        #   Explanation: We can pick from all trees.
        #   Note that we cannot pick from trees 0 and 2 since they have different fruit types.
#
#  *******************************************************************

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        dict1= {}
        max_fruits = 0
        for right in range(len(fruits)):
            if(fruits[right] not in dict1):
                dict1[fruits[right]] = 1
            else:
                x= dict1[fruits[right]]
                dict1[fruits[right]] = x + 1
            while(len(dict1) > 2) :
                x = dict1[fruits[left]]
                if(x>0):
                    dict1[fruits[left]] = x - 1
                if(dict1[fruits[left]]==0):
                    del dict1[fruits[left]]

                left  =  left + 1
            
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

            
        