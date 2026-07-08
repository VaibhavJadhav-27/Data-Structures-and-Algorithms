
# ------------------------------------------------------------------------------------------------------------
# Problem no :  75
# Problem heading :  Sort Colors
# Problem Link : https://leetcode.com/problems/sort-colors/description/

# Problem Description : 
#   You are given an array nums of length n containing only the integers 0, 1, and 2.
#   Sort the array in-place so that all 0s come first, followed by all 1s, then all 2s.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [2,0,2,1,1,0]
#   Output: [0,0,1,1,2,2]
#
#   Explanation: The above array is represented by array [2,0,2,1,1,0]. In this case, the sorted array is [0,0,1,1,2,2].
#   Note that the array is sorted in-place.
#
#  *******************************************************************

# Note: You must solve this problem without using the library's sort function.

# this pattern is called as Dutch National Flag Algorithm. 
# It is a three-way partitioning algorithm that sorts an array of elements into three distinct groups based on a pivot value. 
# The algorithm is named after the Dutch national flag, which has three colors: red, white, and blue. 
# In this case, the three colors are represented by the integers 0, 1, and 2.

# --- bubble sort solution ---
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break  
            
            

# ---------------- optimized solution -------------------
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high = len(nums)-1
        while(mid<=high):
            if(nums[mid]==2):
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1
                continue
            elif(nums[mid]==0):
                nums[mid],nums[low]=nums[low],nums[mid]
                low=low+1
                mid=mid+1
                continue
            else:
                mid=mid+1
                continue
