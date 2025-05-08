
class Solution:

    def getSum(self, a: int, b: int) -> int:
        '''
        - Integers a and b
        - Return the SUM of the two integers
        - Do not use + or -

        - We first understand HOW addition works
        - Adding number a and b results can be 
        broken up into two components
        - Each operation is done on a single column 
        - noCarries(a,b), which is a+b WITHOUT 
        carrying
        - carries(a,b), which is a+b WITH ONLY 
        carries
        - With this model for addition, we would 
        calculate noCarries and carries for a and b
        - Next, we would shift carries to the left 
        column by 1, because it is a carry
        - But then what do we do with our carry
        - One option would be to add, but we will 
        do something interesting
        - We REPEAT, using the sum WITHOUT carries 
        and only carries as our operands
        - This means that some individual carries 
        might propagate way beyond their immediate 
        left column
        - Therefore, we continue this until we have 
        no more carries!

        - Calculating the sum WITHOUT carries
        - Let's go column by column
        - For 1 column, we have bit1 and bit2
        - We want to return 1 if exactly one out of 
        bit1 and bit2 is 1
        - Otherwise we want to return 0
        - This is exactly what our XOR operator 
        does!
        - We can do this on the entirety of a and b
        - sumWithoutCarries = a XOR b

        - Calculating ONLY the carries from 
        summation
        - Let's go column-by-column
        - For 1 column, we have bit1 and bit2
        - We want to return 1 if exactly both bits 
        are 1, else we return 0
        - This is exactly what our AND operator does
        - We can do this on the entirety of a and b
        - onlyCarries = a AND b
        - But these carries are meant to be applied 
        to the bit on the left column!
        - We left bit shift the result
        - onlyCarries = onlyCarries << 1


        - All Python aspects can be understood by the 
        following facts
        - Python represents negative numbers with 
        infinite leading 1s, which must all be operated 
        on
        - A 32-bit register is enough to represent the 
        range of a and b
        - We mask variables that we will reuse
        - All specific underlying concepts are explained 
        on my Notion page
        '''        

        # Set a 32-bit mask, enough for -1000<a,b<1000
        mask = 0xffffffff

        # Operate until there is no more carry
        while b != 0:
            # Find the carry from adding a and b
            carry = (a & b) << 1
            # Find the sum without the carry of a and b
            # We mask a because we will reuse it
            a = (a ^ b) & mask
            # Set b to be the carry
            # We mask since we will reuse it
            b = carry & mask

        if a > (mask >> 1):
            # We have a larger number than the largest 
            # number we can represent
            # So our MSB is on
            # So we have a negative number

            # We XOR a with the mask to flip all bits in 
            # the register

            # We flip all bits 
            # This turns all leading 0s to 1s, so the 
            # number is negative
            # This flips all bits in the register, getting 
            # the original negative number that was stored

            return ~(a ^ mask)
        else:
            # We have leading 0s followed by the number
            # So the representation of a corresponds with 
            # the representation of a that Python would 
            # use
            return a



if __name__ == "__main__":
    sol = Solution()
    a = 1
    b = 1
    print(sol.getSum(a,b)) # 2
    a=4
    b=7
    print(sol.getSum(a,b)) # 11
    a=9
    b=11
    print(sol.getSum(a,b)) # 20