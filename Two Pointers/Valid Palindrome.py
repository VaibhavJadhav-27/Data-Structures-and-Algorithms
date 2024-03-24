# ------------------------------------------------------------------------------------------------------------
# Problem no :  125
# Problem heading :  Valid Palindrome
# Problem Link : https://leetcode.com/problems/valid-palindrome/description/

# Problem Description : 
#   A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
#   it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#   Given a string s, return true if it is a palindrome, or false otherwise.

#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: s = "A man, a plan, a canal: Panama"
#   Output: true
#   Explanation: "amanaplanacanalpanama" is a palindrome.
#   
#  *******************************************************************



#  Approch 1
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = ""
        if(len(s)==0):
            return True
        for i in s:
            if(i.isalnum()):
                str1 = str1 + i
        lowercase_string = str1.lower()
        reversed_string = lowercase_string[::-1]
        if(lowercase_string == reversed_string):
            return True
        return False



        

# Approach 2
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if(len(s)==0):
            return True
        string=''

        for i in s:
            if i.isalnum():
                string+=i.lower()
            else:
                continue
        index_comp=(len(string)+1)//2
        for i in range(index_comp):
            if string[i]==string[len(string)-1-i]:
                continue
            else:
                return False
        return True



