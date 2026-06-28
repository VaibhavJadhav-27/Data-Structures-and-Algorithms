
def TwoSum(nums,target):
    unsorted_list = nums[:]
    nums.sort()
    i=0
    j=1
    while(j<len(nums)):
        if(nums[i] + nums[j]==target):
           i = nums[i]
           j = nums[j]
           print(i," : ")
           break
        elif (nums[i]+nums[j] < target):
            j=j+1
        elif( nums[i]+ nums[j] > target):
            j=j-1
            i=i+1
    if(i==j):
        return [unsorted_list.index(i),unsorted_list.index(j)+1]
    return [unsorted_list.index(i),unsorted_list.index(j)]

input = [3,2,3]
target = 6
ans = TwoSum(input,target)
print(ans)




#----- Optimal Solution -----
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(0, len(nums)):
            x = target - nums[i]
            if(x in dict1):
                return [i,dict1[x]]
            else:
                dict1[nums[i]] = i
        