class Solution:

    def isHappy(self, n: int) -> bool:
        '''
        - A non-cyclical number is defined as such
        - 1. Given a positive integer, replace it 
        with the sum of the squares of its digits 
        - 2. Repeat the above step until the number 
        equals 1, or is loops infinitely in a 
        cycle which does not include 1
        - 3. If it stops at 1, then the number 
        is a non-cyclical number
        - Given a positive integer n, return true 
        if it is a non-cyclical number, otherwise 
        return false

        - Problems
        - Derive a list of digits of an integer
        - Sum the squares of the digits of the 
        integer
        - Find out whether the algorithm will 
        result in a 1 or not

        - Problem: Derive a list of digits of an 
        integer
        - Let n be an integer
        - Use string comprehension to convert n 
        into digits

        - Problem: Replace an integer with the sum 
        of the square of its digits
        - Set n to zero
        - Loop over digits, adding its square to n

        - Find out whether the algorithm will 
        result in a 1 or not
        - Store n in hash set resuls
        - Return False if you see n is already in 
        results

        - My solution is the same in concept, just 
        very slightly different lines
        - So we will use my solution!

        - O(log n) time and space
        -> The number of digits in a number is found 
        in O(log n) time
        -> The possible results collapses quickly
        -> Once you get to, say, <1,000 you now 
        deal with 3 digits
        -> Assuming you get to 999, you get 
        9^2+9^2+9^2 = 243, meaning that 243 provides 
        an upper bound
        '''
        
        # Hash set for results we see
        results = set()

        # Derive a list of digits of an integer
        while n != 1:
            if n in results:
                # Find out whether the algorithm will 
                # result in a 1 or not
                return False
            
            # Add n to results set
            results.add(n)

            # Derive digits from n
            digits = [int(d)*int(d) for d in str(n)]

            # Sum the squares of the digits of 
            # the integer
            n = sum(digits)

        # If we exit, we have found a 1
        return True

if __name__ == "__main__":
    sol = Solution()
    n = 101
    print(sol.isHappy(n)) # False
    n = 100
    print(sol.isHappy(n)) # True
    n = 2
    print(sol.isHappy(n)) # False
