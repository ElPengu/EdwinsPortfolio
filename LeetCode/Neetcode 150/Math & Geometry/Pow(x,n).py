class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        - Pow(x,n)=>x^n
        - Given floating point x and integer n, 
        implement myPow(x,n) function 
        - You may not use any built-in library 
        functions

        
        - There are two solutions, but one does not 
        pass on Leetcode due to its efficiency
        - Solution 1: Iterative multiplication (does 
        not pass on LeetCode due to efficiency)
        - Solution 2: Divide and conquer


        - Solution 1: Iterative multiplication 
        (does not pass on LeetCode due to 
        efficiency) 

        - Problems
        - Implement pow(x,n) when n is positive
        - Implement pow(x,n) when n is zero
        - Implement pow(x,n) when n is negative
        
        - Problem: Implement pow(x,n) when n is 
        positive
        - Set a while loop to multiply x by 
        itself n times

        - Problem: Implement pow(x,n) when n is 
        zero
        - Return 1

        - Problem: Implement pow(x,n) when n is 
        negative
        - Use the solution to problem for when n is 
        positive n times 
        - Return 1/res

        - O(n) time <- Multiplying n times
        - O(1) space <- Storing the result in a variable

        
        - Solution 2: Divide and conquer
        
        - Problems
        - Deal with the case that n is 0
        - Deal with the case that n > 0 and even
        - Deal with the case that n < 0
        
        - Problem: Deal with the case that n is 0
        - Trivial case, return 1

        - Problem: Deal with the case that n > 0 
        and even
        - Consider x^(n) where n is even
        - This can be written as 
        (x^(n/2))*(x^(n/2))
        - These are two identical subproblems
        - We do not want to branch twice, so we 
        solve one of the problems then multiply it 
        by itself
        - There is a neat little trick to save a 
        line of code 
        - Reduced subproblem: x^n=((x*x)^(n/2))
        - We can keep on doing this
        - Therefore we solve this problem 
        recursively until we reach base case n = 1, 
        where we return 1
        - To deal with the odd case, multiply the 
        result by 2, else return the result as is
        
        - Problem: Deal with the case that n < 0
        - Use the solution to the problem of n>0, 
        using the absolute value of n
        - Return the inverse of the solution!

        - O(log n) time <- We divide N (not n) 
        by 2 until it is 1, which is literally 
        log 2 N
        - O(log n) space <- For the call stack
        '''
        
        def helper(x, n):
            # 
            if x == 0:
                # We have base case
                return 0
            if n == 0:
                # x^0 = 1
                return 1

            # We pass in x*x since (x^n)*(x^n) = 
            # (x*x)^n
            res = helper(x*x, n//2)

            # We deal with the case that 
            # we have an odd vs even without 
            # explicitly writing it as a separate 
            # subproblem
            return x*res if n%2 else res

        # Call our helper function
        # Never pass a negative exponent
        res = helper(x, abs(n))

        # Return based on whether we have n is 0
        return res if n >= 0 else 1/res

if __name__ == "__main__":
    sol = Solution()
    x = 2.00000
    n = 5
    print(sol.myPow(x,n)) # 32.00000
    x = 1.10000
    n = 10
    print(sol.myPow(x,n)) # 2.59374
    x = 2.00000
    n = -3
    print(sol.myPow(x,n)) # 0.12500