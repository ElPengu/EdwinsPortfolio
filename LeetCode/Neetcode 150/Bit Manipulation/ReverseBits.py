class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        - 32-bit unsigned integer n
        - Reverse the bits of the binary 
        representation of n
        - Return the result
        
        - Finding the LSB
        - Moving from the current bit to the left 
        bit in n
        - Setting up our res
        - Replacing bit 0 at index i in res with 
        bit j

        - Finding the LSB
        - We perform n AND 1, the result is 0 
        IFF the bit is 0

        - Moving from the current bit to the left 
        bit in n
        - Each time we move to the next bit, we 
        left shift our offset by 1
        - The result is 0 IFF the bit is zero 
        
        - Setting up our res
        - We set res to 0 initially, so in binary 
        it is all 0s

        - Replacing bit 0 at index i in res with 
        bit j
        - Our bit j is a 1 or 0
        - Left bit shift j so that it goes from N-1 
        to i, set j to this new value
        - Set res = res OR j  
        - This works because 0 OR 1 => 1 and 0 OR 0 
        => 0
        - So 0 OR j => j
        - And for the rest of the bits, b OR 0 => b

        - O(1) time <= 32 bits
        - O(1) space <= Single variable
        '''

        # Initialise res
        res = 0

        for i in range(32):
            # For every bit

            # In the explanation we left shift 1
            # You can see here that right shifting 
            # n by i and then AND with 1 has the 
            # same effect as left shifting 1 by i 
            # and then AND with n
            bit = (n >> i) & 1

            # Put the bit in res, starting at the 
            # first bit, all the way on the left
            res = res | (bit << (31-i))

        return res

if __name__ == "__main__":
    sol = Solution()
    n = 0b00000000000000000000000000010101
    print(sol.reverseBits(n)) # 2818572288 (10101000000000000000000000000000)