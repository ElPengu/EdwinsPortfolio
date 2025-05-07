from collections import deque

class Solution:

    def checkValidString(self, s: str) -> bool:

        '''
        - Every '(' must have a corresponding ')' 
        AND VICE VERSA
        - Left parenthesis '(' must occur BEFORE 
        corresponding right parenthesis ')'
        - A * may be treated as a '(', ')' or 
        an empty string ""

        - Is this not solved with a stack?
        - So put every NON-'*' character in the 
        stack
        - Ugh, I kinda forgot how this work
        - Okay, let's assume that we CAN make 
        the stack work
        - We'd keep a count for '*' available
        - Whenever we cannot close or...
        - Wait, the placement of the '*' does 
        matter
        - Hm

        - Let's keep all characters in order
        - Assume that we have a way that works 
        for '(' and ')'
        - If we see a '*', we ask ourselves if 
        we want to use it YET
        - If we must use it, do so
        - How do we know if we must use it?
        - ...

        - Okay I kind of remember the solution
        - You read '(' into a stack, and then 
        when you read ')' you pop and verify 
        that you popped ')'
        - If you don't pop '(' or stack is empty, 
        it is invalid

        - How can '*' be used?
        - If you read...

        - Got an insight 19 mins into the problem!
        - You only care about the number of '*' 
        that you can use SO FAR
        - So just check '*', if you don't want to 
        use it now just save it if you need it 
        because the stack has exhausted its '(' and 
        you need one, or if you have some '(' 
        remaining
        '''

        # Create queue
        q = deque()

        # Count for '*'
        count = 0

        # Read every character
        for c in s:
            if c == '(':
                # If you read a '(', add it to the queue
                q.append(c)

            if c == '*':
                # Increase count
                count += 1

            if c == ')':
                # If you read a ')', check what you pop from the 
                # queue
                if len(q) == 0 and count == 0:
                    # There is nothing to pop, return False!
                    return False
                if len(q) == 0:
                    # Use a *
                    count-=1
                else:
                    # Character can be matched!
                    # Pop from the RIGHT
                    popped = q.pop()
                
        # If the queue is empty return True!
        return len(q)-count <= 0

if __name__ == "__main__":
    sol = Solution()
    s = "((**)"
    print(sol.checkValidString(s)) # True
    s = "(((*)"
    print(sol.checkValidString(s)) # False