# ------------------------------------------------------------------------------------------------------------
# Problem no :  347
# Problem heading :  Top K Frequent Elements
# Problem Link : https://leetcode.com/problems/top-k-frequent-elements/description/

# Problem Description : 
#   Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]
#   Explanation: First find out the count of each element and then return a list of k elements which are having maximum count.
#   
#  *******************************************************************




class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        ans = []
        nums_set = set(nums)
        nums_count = {}
        for i in nums_set:
            nums_count[i] = nums.count(i)
        for i in range(0,k):
            max_key = max(nums_count, key=lambda k: nums_count[k])
            ans.append(max_key)
            nums_count.pop(max_key)
        return ans