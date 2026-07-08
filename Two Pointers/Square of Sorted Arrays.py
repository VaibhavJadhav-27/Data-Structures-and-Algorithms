# ------------------------------------------------------------------------------------------------------------
# Problem no :  977
# Problem heading :  Square of Sorted Arrays
# Problem Link : https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Problem Description :
#   Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Example 1:
#   Input:  nums = [-4,-1,0,3,10]
#   Output: [0,1,9,16,100]
#   Explanation: The squares of the numbers are [16,1,0,9,100], which when sorted give [16,1,0,9,100].
#
#   Example 2:
#   Input:  nums = [-7,-3,2,3,11]
#   Output: [4,9,9,49,121]
#   Explanation: The squares of the numbers are [4,9,9,49,121], which when sorted give [4,9,9,49,121].
#  *******************************************************************


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            ans.append(i*i)
        return sorted(ans)
    
    

# ---------------- optimized solution -------------------

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(nums)
        if(len(nums)==1):
            return [nums[0]*nums[0]]
        i=0
        j=len(nums)-1
        k=len(nums)-1
        while(i<=j):
            if(abs(nums[i])>abs(nums[j])):
                ans[k]=nums[i]*nums[i]
                k=k-1
                i=i+1
            else:
                ans[k]=nums[j]*nums[j]
                k=k-1
                j=j-1
        return ans
            
