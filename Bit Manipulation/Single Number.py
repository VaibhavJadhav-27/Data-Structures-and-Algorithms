
# ------------------------------------------------------------------------------------------------------------
# Problem no :  136
# Problem heading :  Single Number
# Problem Link : https://leetcode.com/problems/single-number/description/ 

# Problem Description : 
#   Given a non-empty array of integers nums, every element appears twice except for one. 
#   Find that single one.
#   You must implement a solution with a linear runtime complexity and use only constant extra space.

 

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [4,1,2,1,2]
#   Output: 4

#   Input: nums = [2,2,1]
#   Output: 1

#  Explanation:
#   Using XOR operation:
#   4 ^ 1 ^ 2 ^ 1 ^ 2 = 4


# Initial: result = 0 (binary: 0000)

# Step 1: result ^= 4
#   0000 ^ 0100 = 0100 (result = 4)

# Step 2: result ^= 1
#   0100 ^ 0001 = 0101 (result = 5)

# Step 3: result ^= 2
#   0101 ^ 0010 = 0111 (result = 7)

# Step 4: result ^= 1  ← Second occurrence of 1
#   0111 ^ 0001 = 0110 (result = 6)

# Step 5: result ^= 2  ← Second occurrence of 2
#   0110 ^ 0010 = 0100 (result = 4) ✓
#  *******************************************************************


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num  # XOR operation: duplicates cancel out, single number remains
        return result
    