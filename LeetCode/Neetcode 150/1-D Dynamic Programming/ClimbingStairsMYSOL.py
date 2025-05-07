class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''
        - We have an integer n
        - n: number of steps to reach the top of a stair case
        - You can climb with either 1 or 2 steps at a time
        - Number of distinct ways?

        - To enumerate all the ways would be O(n) time I think
        - We have two choices!
        - Start at step 0
        - Base case: are we at step n. If so return 1
        - Base case: are we beyond step n. If so return 0
        - Call DFS at step=step+1
        - Call DFS at step=step+2
        '''

        # climb function
        def climb(step):
            # Base cases
            if step == n:
                # We have found a way to climb the stairs
                return 1
            elif step > n:
                # We have found a way to NOT climb the stairs
                return 0
            
            # Find all ways to climb up one step and two steps
            return climb(step+1)+climb(step+2)
        
        # Start at step 0 and return all the distine ways to climb to 
        # top of the stair case
        return climb(0)

if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.climbStairs(n)) # 2
    n = 3
    print(sol.climbStairs(n)) # 3