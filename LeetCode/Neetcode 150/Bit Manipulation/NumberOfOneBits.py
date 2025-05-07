class Solution:
    '''
    - You are given an unsigned integer n
    - Return the number of 1 bits in its 
    binary representation

    - Two solutions, second solution is 
    slightly faster but less intuitive

    - Solution using MOD
    - MOD with 2 to see whether the LSB is 1 
    or 0
    - To consider the number to the left is 1, 
    use a "bit shift"
    - Continue until n is 0

    - Down side: We even look at 0s
    - What if we only looked at 1s?
    
    - O(1) time <- for 32 bits
    - O(1) space <- No extra space is really needed
    
    - Solution using AND
    - Set n = n&(n-1) until n=0
    - Each iteration, we get rid of the LSB that is 
    a 1
    - For each 1 we get rid of, increment res

    - Why the AND solution work for detecting the 
    final 1 bit
    - Consider a number n, ending in a 1 followed 
    by a number of bits b, where b >= 0 AND each 
    bit is itself a 0
    - This makes 1 the LSB that is a 1
    - Form n-1
    - From n, the LSB that is a 1 => 0 in n-1, 
    and the b bits following 1 => 1
    -> This is basically asking what the number 
    before 1000... in binary is, which is 0111...
    - Take n_1 = n AND n-1
    - In n_1, the LSB that is a 1 in n will 
    correspond to 1 AND 0 => 0
    - In n_1, the remaining b bits will correspond 
    to 0 AND 1 => 0
    - In n_1, the prefix to the LSB that is a 1 
    in n remains the same
    - Hence, n = X10..., n-1 = X01..., n_1=X00...

    - We skip all the zeroes in between!

    - O(1) time for checking bits
    - O(1) space, nothing else really used
    '''

    def hammingWeightMOD(self, n: int) -> int:
        
        # Total number of 1s
        res = 0

        while n:
            # Continue until n is 0

            # See if we have a 1 or 0 at the LSB
            res += n % 2

            # Shift everything to the right by 1
            n = n >> 1
        
        return res
    
    def hammingWeightAND(self, n: int) -> int:
        
        # Total number of 1s
        res = 0

        while n:
            # Form n=(n-1)
            n &= (n-1)

            # Increment res
            res+=1
        
        return res

if __name__ == "__main__":
    sol = Solution()
    n = 0b00000000000000000000000000010111
    print(sol.hammingWeightMOD(n)) # 4
    #print(sol.hammingWeight(n)) # 4
    n = 0b01111111111111111111111111111101
    print(sol.hammingWeightMOD(n)) # 30
    #print(sol.hammingWeight(n)) # 30