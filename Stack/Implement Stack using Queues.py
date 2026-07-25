
# ------------------------------------------------------------------------------------------------------------
# Problem no :  225
# Problem heading :  Implement Stack using Queues
# Problem Link : https://leetcode.com/problems/implement-stack-using-queues/description/

# Problem Description : 
#   Implement a stack using two queues.

#   Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#   Implement the MyStack class:
#   - void push(int x) Pushes element x to the top of the stack.
#   - int pop() Removes the element on the top of the stack and returns it.
#   - int top() Returns the element on the top of the stack.
#   - boolean empty() Returns true if the stack is empty, false otherwise.


#-------------------------------------------------------------------------------------------------------------

#  *******************************************************************
#   Input: ["MyStack", "push", "push", "top", "pop", "empty"]
#   Output: [null, null, null, 2, 2, false]
#   Explanation:
#   MyStack myStack = new MyStack();
#   myStack.push(1);
#   myStack.push(2);
#   myStack.top(); // return 2
#   myStack.pop(); // return 2
#   myStack.empty(); // return false

#  *******************************************************************

class MyStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        x = self.stack[-1]
        self.stack.pop()
        return x
        

    def top(self):
        """
        :rtype: int
        """
        if(len(self.stack)>0):
            return self.stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if(len(self.stack)<=0):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()