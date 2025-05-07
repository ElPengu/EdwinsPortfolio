class Solution:

    def partition(self, s: str):
        # Palindrome: written the same backwards
        # as forwards
        # We want all lists of palindromic substrings
        # that build s
        # 
        # The brute force way is the best way...
        # > Backtracking
        # 
        # Consider "aab"
        # The choice of the first partition is either 
        # 1, 2, or 3 characters
        # > This results in three branches
        # Whenever a branch results in a NON-PALINDROMIC
        # substring, we stop exploring the branch
        # Else, we make all possible choices until the 
        # branch is exhausted!
        # 
        # We use recursive DFS to do this. Keep a pointer
        # index so that we know where to look for 
        # palindromes for (from length 1 to end of the 
        # string!)
        # 
        # O(2^n) time complexity, for all possible strings

        # Stores all possible partitions
        res = []

        # This is for our current partition
        part = []

        def dfs(i):
            # Check the base case

            if i >= len(s):
                # We are out of bounds

                # Add a copy of par to res
                res.append(part.copy())
                return

            # We make all possible choices for substrings
            for j in range(i, len(s)):
                # If this is a palindrome, add it
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    # dfs to look for additional 
                    # palindromes
                    dfs(j+1)
                    
                    # Clean up par
                    part.pop()

        # Call dfs on index 0
        dfs(0)

        return res
    
    # Checks if we have a palindrome
    def isPali(self, s: str, i: int, j: int)->bool:
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    print(sol.partition(s)) # [["a","a","b"],["aa","b"]]
    s = "a"
    print(sol.partition(s)) # [["a"]]