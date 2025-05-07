from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        - Integer n
        - Count the number of 1s in its binary 
        representation in range [0,n]
        - Return array output where output[i] 
        is the number of bits in binary 
        representation of i

        - There is an O(n log n) solution
        - There is a more efficient O(n) solution 

        - O(n log n) solution
        - Loop over every number <- O(n) time
        - The number of digits in a number i 
        occupies O(log i) space
        - Therefore to count the digits of i 
        will take O(log i) time
        - We do O(log i) n times, with i varying
        - Leading to O(n log n)

        - O(n) solution
        - Let's map 0,3 to binary
        - [0,1,2,3]=>[0000,0001,0010,0011]
        - So we have bit 1 appear 0,1,1,2
        - Let's map 4,6 to binary
        - [4,5,6,7]=>[0100,0101,0110,0111]
        - You see that we have the mapping for 1,3, 
        but with an extra bit 1
        - So we have bit 1 appear
        1+dp[4-4], 1+dp[5-4], 1+dp[6-4], 1+dp[7-4]
        - How about 8?
        - 8=>1000
        - We see that the number of 1 bits is 
        1+dp[8-8]
        - The pattern to spot is that each time 
        we introduce a new MSB, the way we access 
        our cache changes
        - 0=>0 <= Base case
        - 1=>1+dp[n-1] <= 2^0 = 1
        - 2=>1+dp[n-2] <= 1 * 2 = 2
        - 3=>1+dp[n-2]
        - 4=>1+dp[n-4] <= 2 * 2 = 4
        - 5=>1+dp[n-4]
        - ...
        - 8=>1+dp[n-8] <= 4 * 2 = 8
        - ...
        - 16=>1+dp[n-16] <= 8 * 2 = 16
        - We define our offset to be this next 
        power, making the pattern in this solution 
        a LOT easier to grasp 
        - 0=>0 <= Base case
        - 1=>1+dp[n-offset] <= Offset = 1
        - 2=>1+dp[n-offset] <= Offset = 2 <= 
        2=offset*2
        - 3=>1+dp[n-offset] 
        - 4=>1+dp[n-offset] <= Offset = 4 <= 
        4=offset*2
        - 5=>1+dp[n-offset]
        - ...
        - 8=>1+dp[n-offset] <= Offset = 8 <= 
        8=offset*2
        - ...
        - 16=>1+dp[n-offset] <= Offset = 16 <= 
        16=offset*2
        - We get a new MSB if we get to the NEXT 
        power of 2
        '''

        # Set our dp array for n+1 values
        dp = [0]*(n+1)

        # Keep offset - highest power of 2
        offset = 1

        for i in range(1, n+1):
            if offset*2 == i:
                # Check if we are at the next power 
                # of 2
                offset = i
            
            # Use the cache to find the number of 
            # 1s
            dp[i] = 1+dp[i-offset]
        
        return dp

            

if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.countBits(n)) # [0,1,1,2,1]