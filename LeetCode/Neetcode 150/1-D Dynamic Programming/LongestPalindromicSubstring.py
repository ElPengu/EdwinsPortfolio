class Solution:

    def longestPalindrome(self, s: str) -> str:
        
        '''
        - We want the longest substring that is a 
        palindrome
        - Palindrome: Reads the same forwards and 
        backwards
        - If there are multiple return any ONE of 
        them

        - To check if a substring is a palindrome is
        linear time
        - There are n2 substrings to check so quadratic
        time
        - This brings up to O(n3) time

        - We can do better!
        - For a palindrome "bab" we could start from 'a' 
        and expand outwards. a -> b+a+b-> "bab"
        - This is helpful!

        - We will consider each character as the centre
        -> n <- Each character
        -> n <- Expand outwards for each characters
        -> O(n2) time

        - There is one edge case: What about palindromes 
        of EVEN length? We'll deal with this by considering
        PAIRS of palindromes

        - Range over characters
        - ODD CASE: Use left and right pointers set to index i
        - EVEN CASE: Use left and right pointers set to indices
        i and i+1
        '''

        res = ""
        # Set longest length to zero
        resLen = 0

        for i in range(len(s)):
            # ODD LENGTH
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # We are at a palindrome
                if r-l+1 > resLen:
                    # We have found a larger palindrome!
                    res = s[l:r+1]
                    # Update resLen
                    resLen = r-l+1
                # Expand left and right
                l-=1
                r+=1
            
            # EVEN LENGTH
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # We are at a palindrome
                if r-l+1 > resLen:
                    # We have found a larger palindrome!
                    res = s[l:r+1]
                    # Update resLen
                    resLen = r-l+1
                # Expand left and right
                l-=1
                r+=1

        
        return res



if __name__ == "__main__":
    sol = Solution()
    s = "ababd"
    print(sol.longestPalindrome(s)) # "bab" or "aba"
    s = "abbc"
    print(sol.longestPalindrome(s)) # "bb"