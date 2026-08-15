
# ------------------------------------------------------------------------------------------------------------
# Problem no :  875
# Problem heading :  Koko Eating Bananas
# Problem Link : https://leetcode.com/problems/koko-eating-bananas/description/

# Problem Description : 
#   Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#   Koko can decide her banana eating speed k (bananas per hour). Each hour, she chooses some pile of bananas and eats k bananas from it. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas in that hour.
#   Return the minimum integer k such that she can eat all the bananas within h hours.

#  *******************************************************************
#   Input: piles = [3,6,7,11], h = 8
#   Output: 4
#   Explanation: Koko can eat all bananas within 8 hours at a speed of 4 bananas per hour.

#   Input: piles = [30,11,23,4,20], h = 5
#   Output: 30
#   Explanation: Koko needs to eat at a speed of 30 bananas per hour to finish all piles within 5 hours.

 
#  *******************************************************************

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        while left <= right:

            mid = left + (right - left) // 2

            # calculate total hours needed at speed mid
            total_hours = 0
            for i in piles:
                hour =  (i + mid - 1)//mid
                total_hours = total_hours + hour

            if total_hours <= h:
                # mid works
                # try smaller speed
                right = mid - 1
            else:
                # mid doesn't work
                # need larger speed
                left = mid + 1

        return left