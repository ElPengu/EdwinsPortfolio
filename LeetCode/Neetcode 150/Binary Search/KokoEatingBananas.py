import math

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int)-> int:
        # We can work from a brute force solution to binary search 
        # solution!
        # 
        # There are n piles
        # Koko has h hours to eat **every** banana
        # Koko can eat up to k bananas from a specific pile at a time
        # Minimize integer k
        # 
        # Brute force solution: Set k to 1, and iterate through every pile
        # Naturally, pile i takes ceil(pile[i]/k). 
        # Finding k takes O(m*m)
        # 
        # We note that 1 <= k <= max(piles)
        # 
        # We can use binary search to try different values of k 
        # in O(log m) time. 
        # Each time we can iterate through piles and see how many hours 
        # it takes in O(n)
        # 
        # Hence, we can do this in O(n*log m) which is ideal!

        # Set left and right pointers
        l, r = 1, max(piles)
        # Our result is detatched from the actual midpoint variable 
        res = r

        # We start binary searching while left <= right
        while l <= r:
            k = l + ((r-l)//2)
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                # We set res in this way so that when r goes 
                # below k, we have the real result
                res = min(res, k)
                
                # If we have taken less than h hours, we update 
                # we minimize k by shifting r down
                r = k-1
            
            else:
                # In this case our k is too small. We start looking 
                # for a larger k
                l = k + 1
        
        # We return result
        return res 


if __name__ == "__main__":
    sol = Solution()
    piles = [1,4,3,2]
    h = 9
    print(sol.minEatingSpeed(piles, h)) # 2
    piles = [25,10,23,4]
    h = 4
    print(sol.minEatingSpeed(piles, h)) # 25