class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        - 32-bit unsigned integer n
        - Reverse the bits of the binary 
        representation of n
        - Return the result
        
        - Get the LSB
        - Right shift n
        - Repeat until n is zero

        - Let LSB = i
        - Append it to a list of strings
        - Return it as a number
        '''

        # 32 BITS
        res = [0]*32
        i = 0
        while i < 32:
            res[i] = str(n%2)
            n = n >> 1
            i+=1

        res = "".join(res)

        res = int(res)

        return res

if __name__ == "__main__":
    sol = Solution()
    n = 0b00000000000000000000000000010101
    print(sol.reverseBits(n)) # 2818572288 (10101000000000000000000000000000)