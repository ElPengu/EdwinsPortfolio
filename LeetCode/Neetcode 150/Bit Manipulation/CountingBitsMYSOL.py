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

        - Problems
        - Find the binary representation of a 
        single number
        - Count the number of 1s in that binary 
        representation
        
        - Find the binary representation of a 
        single number
        - Unnecessary, Python will automatically 
        do so

        - Count the number of 1s in that binary 
        representation
        - For every i, set count=0
        - Keep setting i=i&(i-1) until i is zero
        - Increment count each time

        '''
        
        # Create list
        res = []

        # Loop from 0 up to n (inclusive)
        for i in range(n+1):
            count = 0
            
            # Apply & to i and i-1 until you 
            # reach zero    
            j = i
            while j:
                j&=(j-1)
                count+=1
            res.append(count)

        return res

if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.countBits(n)) # [0,1,1,2,1]