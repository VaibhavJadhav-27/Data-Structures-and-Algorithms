
# ------------------------------------------------------------------------------------------------------------
# Problem no :  345
# Problem heading :  Reverse Vowels of a String
# Problem Link : https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# Problem Description : 
#   Given a string s, reverse only all the vowels in the string and return it. 
#   The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "IceCreAm" 
#   Output: "AceCreIm" 
#   Explanation:

#   The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
#  *******************************************************************


class Solution(object):
    def findingVowels(self, s, vowels):
        lst=[]
        for i in s:
            if(i in vowels):
                lst.append(i)

        lst=lst[::-1]
        return lst

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        lst = self.findingVowels(s,vowels)
        j=0
        temp=list(s)
        for i in range(0,len(temp)):
            if(temp[i] in vowels):
                temp[i] = lst[j]
                j=j+1
        result = ''.join(temp)
        return result


    
