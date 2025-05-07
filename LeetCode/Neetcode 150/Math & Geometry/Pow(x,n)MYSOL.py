class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        - Pow(x,n)=>x^n
        - Given floating point x and integer n, 
        implement myPow(x,n) function 
        - You may not use any built-in library 
        functions

        - Problems
        - Implement pow(x,n) when n is positive
        - Implement pow(x,n) when n is zero
        - Implement pow(x,n) when n is negative
        
        - Problem: Implement pow(x,n) when n is 
        positive
        - Set a while loop to multiply x by 
        itself until n is zero

        - Problem: Implement pow(x,n) when n is 
        zero
        - Return 1

        - Problem: Implement pow(x,n) when n is 
        negative
        - Use the solution for when n is positive 
        - Return 1/res
        '''
        # Set res
        res = 0

        # Implement pow(x,n) when n is zero
        if n == 0:
            # Base case
            return 1
        
        isPositive = n>0

        # Implement pow(x,n) when n is positive
        res = x
        if isPositive:
            while n > 1:
                res*=x
                n-=1
        else:
            while n < -1:
                res*=x
                n+=1

        # Implement pow(x,n) when n is negative
        return res if isPositive else 1/res

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