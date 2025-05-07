class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''

        - This is a pretty easy dynamic programming 
        problem!

        - We have an integer n
        - n: number of steps to reach the top of a stair case
        - You can climb with either 1 or 2 steps at a time
        - Number of distinct ways?

        - Recursion seems attractive, however this 
        would take O(2^n) time. 
        - This DFS method repeats calculations 
        WHENEVER you reach a certain step

        - EXAMPLE OF SAME SUBPROBLEM
        - Start at step 0. On the left take two 
        single steps, on the right take one double 
        steps
        - These subtrees will LITERALLY be IDENTICAL
        
        - We take advantage of this by using 
        memoizing the paths from EVERY step once
        - O(n) time!

        - We will use a BOTTOM-UP dynamic programming
        approach
        -> We will start at the base case of the nth
        step, then go back 1 at a time

        - We will store our results in an array DP 
        s.t. at ith index we have the number of paths 
        from step i

        - At DP[n] you store 1 because you are 
        already there
        - At DP[n-1] you store 1 because you could 
        take a SINGLE step
        - At DP[i] we look FORWARD to DP[i+1] and
        DP[i+2]
        - Since we have COMPUTED how many paths we 
        could take from DP[i+1] and DP[i+2], we just 
        store the sum of them
        - Solution will be in DP[0]

        - This is basically the Fibonnaci sequence!

        - We now have O(n) space, but we can reduce
        to O(1) space
        
        - Initialise variables ONE and TWO
        - DP[n-1] = ONE, DP[n] = TWO
        - Shift ONE and TWO until ONE has shifted
        to DP[0]
        - Loop n-1 times
        - Return ONE

        '''

        # Store variables one and two
        one, two = 1,1

        # one = DP[n-1]
        # two = DP[n]

        for i in range(n-1):
            # We loop n-1 times to bring one down
            # from DP[n-1] to DP[0]
            
            # Store one in temporary variable
            temp = one
            # Store sum of one and two in one
            one = one+two
            # Store two as original one value
            # I.e., temp
            two = temp

        # One will hold number of paths from 0
        return one

if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.climbStairs(n)) # 2
    n = 3
    print(sol.climbStairs(n)) # 3