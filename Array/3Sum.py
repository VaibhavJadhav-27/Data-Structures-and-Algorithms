
# ------------------------------------------------------------------------------------------------------------
# Problem no :  15
# Problem heading :  3Sum
# Problem Link : https://leetcode.com/problems/3sum/description/

# Problem Description : 
#   Given an array of integers, find all unique triplets in the array which gives the sum of zero.
#   Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]
#   Explanation:
#   Explanation: 
#   nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#   nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#   nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#   The distinct triplets are [-1,0,1] and [-1,-1,2].
#   Notice that the order of the output and the order of the triplets does not matter.

#   Input: nums = [0,1,1]
#   Output: []
#   Explanation: The only possible triplet does not sum up to zero.
#  *******************************************************************


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp=sorted(nums)
        ans=[]
        for x in range(0,len(nums)-2):
            i=x+1
            j=len(nums)-1
            if(x>0 and temp[x]==temp[x-1]):
                continue
            else:
                while(i<j):
                    add = temp[x] + temp[j] + temp[i]
                    if(add==0):
                        ans.append([temp[x],temp[i],temp[j]])
                        i=i+1
                        j=j-1

                        while(i <j and temp[i]==temp[i-1]):
                            i=i+1
                            
                        while(i<j and temp[j]==temp[j+1]):
                            j=j-1

                        #break
                    elif(add>0):
                        j=j-1
                    else:
                        i=i+1
        return ans

        