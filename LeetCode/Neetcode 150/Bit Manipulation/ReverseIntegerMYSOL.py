class Solution:
    def reverse(self, x: int) -> int:
        '''
        - You are given a signed 32-bit integer x
        - Return x after reversing each of its 
        digits
        - After reversing, if x goes outside the 
        signed 32-bit integer range [-2^31,2^31 -1] 
        then return 0 instead
        - Solve the problem without using integers 
        that are outside the signed 32-bit integer 
        range

        - I really have a shakey solution, but 
        let's go

        - I'd mod x by 10 for the remainder, convert 
        it to bits, and add it to res
        - Then I'd set x = x//10

        - Okay, I have an idea, but coding it up is 
        so involved
        - I'd convert x mod 10 into bits
        - I would add x mod 10 left bit shifted i 
        times to res
        - I would set x = x//10

        - Ugh, bit manipulation! At least it is the 
        final problem of the Neetcode 150!
        
        '''

        res = 0

        # The index at which we add to res
        i = 0

        while abs(x)>1:
            # Find remainder when dividing by 10
            r = x%10
            # Left shift to the correct position
            bits = r << i

            # Add bits to res
            while bits:
                # Find carry
                tmp = (res & bits) << 1
                # Find sum without carry
                res = res ^ bits
                # Set carry
                bits = tmp

            # Remove remainder from x when dividing 
            # by 10
            x = x//10

            i += 1
        
        return res

if __name__ == "__main__":
    sol = Solution()
    x = 1234
    print(sol.reverse(x)) # 4321
    sol = Solution()
    x = -1234
    print(sol.reverse(x)) # -4321
    x = 1234236467
    print(sol.reverse(x)) # 0