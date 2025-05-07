from typing import List

class Solution:

    def evalRPM(self, tokens: List[str]) -> int:
        # The tokens list can be treated like a stack
        # The operation is always applied to the 
        # two previous operands, and once 
        # an operation and the two preceding 
        # operands are used, they are removed 
        # and the result is put in its place
        # 
        # Consider [3,2,-,5,*]
        # -> [(3-2),5,*]
        # -> [1,5,*]
        # -> [5]
        # 
        # We create a stack and read tokens 
        # into the stack, and once we read 
        # an operation token we perform the 
        # operation on the last two added 
        # elements of the stack, pop them 
        # off, and append the result!
        #

        # 1. Create the stack
        stack = []

        # 2. Loop over all tokens
        for c in tokens:
            # If we see an operation we pop off the 
            # last two elements in the stack 
            # and append the result of that operation 
            # on them
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            
            # If we do NOT see an operation, we are 
            # at a number. Append it as usual
            else:
                stack.append(int(c))

        # 3. If it is valid RPN, the stack should 
        # only have the result
        return stack[0]


if __name__ == "__main__":
    sol = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    print(sol.evalRPM(tokens)) # 5
