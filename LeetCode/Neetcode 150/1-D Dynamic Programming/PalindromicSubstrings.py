class Solution:

    def countSubstrings(self, s: str) -> int:
        '''
        - We want the number of palindromes in s
        - We have two cases for palindromes

        - EVEN CASE: A palindrome prepended and appended
        with the same character, BASE CASE single character
        - ODD CASE: A palindrome prepended and appended
        with the same character, BASE CASE pair of characters

        - We will loop over characters and use two pointers

        - n <- to expand from base case
        - n <- number of base cases
        - O(n2)

        - In 12 1/2 minutes too!

        - In the coded example we will use a helper
        function to abstract the odd and even cases 
        to reduce repeated code 
        '''

        # Count for substrings
        res = 0

        for i in range(len(s)):

            # ODD LENGTH
            res += self.countPali(s, i, i)

            # EVEN LENGTH
            res += self.countPali(s, i, i+1)
         

        return res


    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # New palindrome!
            res+=1
            # Update left and right pointers
            l-=1
            r+=1

        return res


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    print(sol.countSubstrings(s)) # 3
    s = "aaa"
    print(sol.countSubstrings(s)) # 6
