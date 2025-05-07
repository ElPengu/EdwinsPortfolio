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

        - Let's look at the subproblem of no '*'
        - Consider (()(()))
        - This can be evaluated using a LIFO 
        structure like a stack
        - When you see a '(' you add it to the 
        stack
        - When you see a ')' you immediately match 
        it with the last seen '('
        - Think about evaluating (), that is what 
        you are doing!
        - A useful insight is that if you see more 
        ')' than '(' at any point then the string 
        is NOT valid
        -> Consider ())(), at ())->)<-() we know 
        that it is so, so over

        - BRUTE FORCE
        - Consider (*)
        - We see the '(' which we must choose
        - We see the '*' giving us three choices
        - BRANCH 1: "()"
        - BRANCH 2: "(("
        - BRANCH 3: "("
        - We see the ')' which we must choose
        - BRANCH 1: "())" <- FAIL
        - BRANCH 2: "(()" <- FAIL
        - BRANCH 3: "()" <- SUCCEED
        - O(3^n) time <- At worst you choose three 
        times

        - This is a difficult problem which requires 
        a trick (but I figured out my own solution!!!)
        - We know that we must always hold more '('
        than ')', so we create "left"
        - left: integer storing how many more '(' than 
        ')' we have seen by index i
        - If you see '(' increment left
        - If you see ')' decrement left
        - Don't worry, this is basically abstracting 
        what the stack would do!
        
        - Now we worry about the '*', which could be 
        '(' or ')' or ''
        - This hints that we need three variables for 
        the range of possible ways that we could 
        select '*'
        - If 0 is in this range after reading s, then 
        we have a valid string!
        - With this insight, we realise that we don't 
        need to consider '*'=='', doing so will 
        be implicitly stored in the range of what 
        left could be by setting '*' to '(' vs setting 
        '*' to ')'
        - leftMax: What is the maximum '(' by setting 
        '*' to '('
        - leftMin: What is the minimum '(', by setting 
        '*' to ')' 
        
        - It is useful to understand two cases for how 
        leftMin and leftMax must be treated specially
        - See below for examples to understand how and 
        why

        - Okay, let's start reading "(*)*()"
        - i=0: leftMin,leftMax=1,1
        - i=1: leftMin,leftMax=0,2
        - i=2: leftMin,leftMax=-1,1
        - Whoa, hold on, we don't want to store invalid 
        ways that we could select '(' EVER!
        - leftMin = max(leftMax,0)
        - leftMin = 0
        - If you don't understand this (I do as of 
        writing this) Neet says that the example 
        s=(*)( should help
        - But what if leftMin crosses over leftMax? 
        Refer to the second example to alleviate 
        your concerns
        - i=3: leftMin,leftMax=-1,2
        - leftMin = max(leftMax,0)
        - leftMin = 0
        - i=4: leftMin,leftMax=1,3
        - i=5: leftMin,leftMax=0,2
        - return 0>=leftMin and 0<=leftMax

        - Now let's read "))(("
        - i=0: leftMin,leftMax=-1,-1
        - Whoa, if leftMax<0 return False!
        
        - In 20 1/2 minutes!!!
        '''

        # Set leftMin and leftMax
        leftMin, leftMax = 0,0

        for c in s:
            if c == "(":
                # We must increment
                leftMin, leftMax = leftMin+1,leftMax+1
            elif c == ")":
                # We must decrement
                leftMin, leftMax = leftMin-1,leftMax-1
            else:
                # Wild card spotted!
                leftMin, leftMax = leftMin-1, leftMax+1
            if leftMax<0:
                # It is straight up impossible for s 
                # to be valid
                return False
            if leftMin<0: # else s = (*)( would be true
                # Interestingly, since leftMax must 
                # be at least 0, we can reset 
                # leftMin
                leftMin = 0
        
        return leftMin == 0


if __name__ == "__main__":
    sol = Solution()
    s = "((**)"
    print(sol.checkValidString(s)) # True
    s = "(((*)"
    print(sol.checkValidString(s)) # False