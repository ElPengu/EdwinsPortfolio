from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # Back tracking way
        # Empty list -> list with one '(' -> two branches, two open or 1 open
        # or one close -> essentially branch out for choosing the next choice 
        # to make
        # Here is an example of how branching works for this backtracking. Note how we add one element at a time 
        # based on the count of open vs closing
        # []
        # -> [(]
        # ->> [((]
        # ->>> [(()]
        # ...
        # ->>> [(((]
        # ...
        # ->> [()] (ONLY ONE CHOICE)
        # ->>> [()(]
        # ...
        # 
        # So we use recursion to reflect these choices. 
        # In our code, we will allow every condition to 
        # be considered at every branch, so that only 
        # valid choices from that branch are made
        
        # Stack to hold parentheses
        #List of valid combinations
        # Note that both are global variables!
        stack, res = [], []

        #We must pass open and closed numbers to this function
        def backtrack(openN, closedN):
            #We break this into the three conditions
            # Base case: n open and closed parentheses
            # Case 1: More open parentheses added than closed -> you 
            # can add either type of parenthesis
            # Case 2: Same number of open and closed parenthesis added ->
            # you must add an open parenthesis
            if openN == closedN == n:
                # We only enter this state when the counts are empty 
                # This means that there are no more parentheses to add 
                # for this branch. So we add to the stack and return
                # By returning, we force our way back up the branches
                res.append("".join(stack))
                return
            
            if openN < n:
                # We append an open parenthesis as long as 
                # there are open parentheses to add
                stack.append("(")
                # Explore more branches with these 
                # updated counts!
                backtrack(openN + 1, closedN)
                # At this point we EXIT the branch. 
                # So we pop off the element added by this 
                # code block
                stack.pop()

            if closedN < openN:
                #We append a closing parenthesis ONLY 
                # if there are already more open 
                # parentheses
                stack.append(")")
                # Explore more branches with these 
                # updated counts!
                backtrack(openN, closedN+1)
                # At this point we EXIT the branch. 
                # So we pop off the element added by this 
                # code block
                stack.pop()

        # We call the backtracking function on initial 0 open and 
        # closed counts
        # This is because we check how openN and closedN compare 
        # to n and only increment these counts. 
        # Alternatively these could be n if we were decrementing 
        # to zero
        backtrack(0,0)
        return res



if __name__ == "__main__":

    sol = Solution()
    print(sol.generateParenthesis(n=1)) # ["()"]
    print(sol.generateParenthesis(n=3)) # ["((()))","(()())","(())()","()(())","()()()"]
