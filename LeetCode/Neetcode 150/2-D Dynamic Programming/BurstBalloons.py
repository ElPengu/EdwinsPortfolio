from typing import List

class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        '''
        - This is definitely a HARD problem
        - How would you answer this if you saw it for the 
        first time in an interview? "I don't have the answer to 
        it" <- NEET

        - Nums is list of integers
        - ith element is balloon with value nums[i]
        - You must burst all of the balloonw
        - If you burst the ith balloon, you receive 
        -> nums[i-1]*nums[i]*nums[i+1]
        - If j=i-1 OR i+1 is out of bounds, nums[j]=1
        - Find the maximum number of coins

        - EXAMPLE
        - nums: [4,*2*,3,7]->[4,*3*,7]->[*4*,7]->[*7*]->0
        - coins: (4*2*3)+(4*3*7)+(1*4*7)+(1*7*1)=143

        - BRUTE FORCE
        - Let's say we have 3,1,5,8
        - We could have trees for popping 3, 1, 5, or 8
        - The tree for popping 3 could choose to pop 1, 5, or 8
        - O(n^n) time, not very good

        - INNEFICIENT SUBPROBLEM 1
        - You first thought might be to store answers for all 
        possible ways of popping the balloons
        - Let's say we pop 1 in [3,1,5,8], now we have subproblem 
        [3,5,8], we can pop again, and again
        - Or we could pop 5 in [3,1,5,8], now we have subproblem 
        [3,1,8]
        - We could pop 1,8 in [3,1,5,8], now we have subproblem 
        [3,5,8]
        - You can choose to either include or disclude a balloon in 
        a subproblem, leading to 2^n space complexity
        - O(2^n) space is not very good 

        - INEFFICIENT SUBPROBLEM 2
        - With [3,1,5,8], let's pop 1 first
        - Now we'll generate TWO subproblems
        -> [3,1] and [8]
        - Now we have n^2 space complexity
        - We cannot independently solve [3,1]
        - However, in reality, we have [3,1] AND [8] as they are 
        connected

        - EFFICIENT SUBPROBLEM
        - Let us use REVERSE THINKING
        - With [3,1,5,8], let's pop 5... LAST
        - 1*5*1 is 5, and we have [3,1] and [8] remaining
        - Now think, will these two subproblems be connected? No!
        - Since we pop 5 LAST, every balloon before it must have 
        been popped, meaning that the right-most element seen by these 
        balloons would be that 5!
        - Similarly, every balloon after 5 must have been popped, 
        meaning that the left-most element seen by these balloons would 
        be that 5
        - [3,1] and [8] would NEVER see each other!
        - So we can pop [3,1] and [8] independently
        - For [3,1], how do we recognise the 5 at the end?
        - Well go back to the problem. In effect, we have two unpoppable 
        balloons with value 1
        -> 1,[3,1,5,8],1
        - We just make the 5 unpoppable
        - Subproblem [3,1] becomes 1,[3,1],5
        - Subproblem [8] becomes 5,[8],1

        - DYNAMIC PROGRAMMING
        - Let DP be cache where DP[L][R]->X
        - L is the left boundary value, and R is the right boundary 
        value
        - We start with L=1, R=N-1
        - Implicit balloons of value 1 are at L=0, R=N
        - Let's say we start with [3,1,5,8] and pop 3 LAST
        - First of all, at the point of popping 3, we do the following
        - nums[L-1]*3*nums[R+1]
        -> We multiply 3 by the implicity balloons 1 at L-1,R+1
        <- I.e., at 0,N
        - Secondly, we deal with the subproblems
        - We are at 3, so we see that the left subproblem is empty
        - The right subproblem is [1,5,8], so we want to know for 
        DP[L+1][R]
        -> Where the left boundary is L+1 and the right boundary is the 
        same
        - So the answer is nums[L-1]*3*nums[R+1]+DP[L+1][R]
        - What if DP[L+1][R] does not exist?
        - We do DFS(L+1,R)

        - How about a more general case?
        - Let's say we pop 1 LAST in [3,1,5,8]
        - nums[L-1]*1*nums[R+1]+DP[i+1][R]+DP[L][i-1]
        - We'll look at the components
        - nums[L-1]*1*nums[R+1]
        -> We pop 1 last, so only L-1 (value 1) and R+1 (value 1) will 
        be used
        - DP[i+1][R]
        -> Here we shift the left pointer up. The left boundary will be 
        pointed to by i, i.e. 1
        - DP[L][i-1]
        -> Here we shift the right pointer down. The right boundary will 
        be pointed to by i, i.e. 1

        - Why is time complexity O(n^3)
        - Let's say that [3,1,5,8] itself is a subarray
        - For every subarray, we must consider each balloon being popped 
        LAST in turn, hence n times
        - We have n^2 subarrays to generate too
        - O(n^3) <- O(n)+O(n^2)

        - O(n^3) time
        - O(n^2) space
        '''

        # Add unpoppable balloons
        nums = [1]+nums+[1]

        # Cache
        dp = {}

        def dfs(l,r):
            # BASE CASES
            if l > r:
                # We have ran out of balloons to pop
                return 0
            if (l,r) in dp:
                # We use what we have stored
                return dp[(l,r)]
            
            # Assume it is 0
            dp[(l,r)] = 0

            for i in range(l,r+1):
                # How many coins if we pop i last
                coins = nums[l-1]*nums[i]*nums[r+1]

                # Now what do we get for the left and right subarrays
                coins+=dfs(l,i-1)+dfs(i+1,r)

                # Possibly update dp
                dp[(l,r)] = max(dp[(l,r)], coins)

            # Return what dp now stores
            return dp[(l,r)]
        # We must start at l=1, r=len(nums)-2 as poppable balloons
        return dfs(1,len(nums)-2)

if __name__ == "__main__":
    sol = Solution()
    nums = [4,2,3,7]
    print(sol.maxCoins(nums)) # 143