
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


        - Now that we have that covered, let's look at 
        the Python-specific aspects to this code
        - Python does NOT automatically deal with 
        overflow, therefore we use a mask so that we 
        overflow at 32 bits
        - Our mask is set at this overflow value: 2^32 -1
        - When we set a and b, we AND with the mask
        - Therefore any bits outside our 32 bit range will 
        be set to 0, all inside will be unaffected
        - Why not AND tmp with our mask? 
        - We could, but we only set it up as our carry for 
        b
        - So when we set b, our tmp may overflow, but we 
        remove those pesky 1's at the end
        
        - By the end our a may be positive or negative
        - If a is positive we can return it
        - If a is negative... we need to be able to detect 
        this
        - This is equivalent to saying that we are larger 
        than the largest positive 32-bit integer
        - The largest positive 32-bit integer is 2^31 -1
        -> mask//2
        - Exceeding mask//2 means that our 32nd bit from 
        the RIGHT is 1, meaning that we have a negative 
        number!
        - We currently have infinite zeroes, then a in two's 
        complement
        - Python represents negative numbers with infinite 0s
        - We want to have infinite 1s, then a in two's 
        complement
        - First, get a in twos complement 
        '''        

        mask = 0xffffffff

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
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