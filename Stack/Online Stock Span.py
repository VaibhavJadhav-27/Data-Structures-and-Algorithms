
# ------------------------------------------------------------------------------------------------------------
# Problem no :  901
# Problem heading :  Online Stock Span
# Problem Link : https://leetcode.com/problems/online-stock-span/description/

# Problem Description : 
#   Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
#   The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
#   For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
#   Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

#   Implement the StockSpanner class:

#   StockSpanner() Initializes the object of the class.
#   int next(int price) Returns the span of the stock's price given that today's price is price.
 

#  *******************************************************************
#   Input:  ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
#           [[], [100], [80], [60], [70], [60], [75], [85]]
#   Output: [null, 1, 1, 1, 2, 1, 4, 6]

#   Explanation:
#   StockSpanner stockSpanner = new StockSpanner();
#   stockSpanner.next(100); // return 1
#   stockSpanner.next(80);  // return 1
#   stockSpanner.next(60);  // return 1
#   stockSpanner.next(70);  // return 2
#   stockSpanner.next(60);  // return 1
#   stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
#   stockSpanner.next(85);  // return 6
#  *******************************************************************

class StockSpanner(object):

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.stack.append(price)
        count = 0
        print(self.stack)
        i =len(self.stack)-1
        while(i>=0):
            print("value of stack[i]:", self.stack[i]," and price : ", price)
            if(self.stack[i]<=price):
                count = count + 1
                print("count ", count)
                i=i-1
            else:
                break
        return count
    

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#  ------- Optimized Solution -----------
class StockSpanner(object):

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while(self.stack and self.stack[-1][0] <= price):
            span = span + self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)