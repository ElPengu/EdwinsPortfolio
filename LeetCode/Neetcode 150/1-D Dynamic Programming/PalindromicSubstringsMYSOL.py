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
        '''

        # A count for palindromic substrings
        count = 0

        # Store the minimum and maximum indices
        MININDEX, MAXINDEX = 0, len(s)-1

        for i in range(len(s)):
            # Loop over index of each character

            # ODD CASE
            l, r = i, i

            while (l >= MININDEX and r <= MAXINDEX and
                   s[l] == s[r]):
                # We are in bounds and we can generate a new
                # palindrome with the characters at the left 
                # and right indices

                count+=1

                # Update left and right pointers
                l-=1
                r+=1

            # EVEN CASE
            l, r = i, i+1

            while (l >= MININDEX and r <= MAXINDEX and
                   s[l] == s[r]):
                # We are in bounds and we can generate a new
                # palindrome with the characters at the left 
                # and right indices

                count+=1

                # Update left and right pointers
                l-=1
                r+=1
                


        # Number of palindromic substrings seen
        return count


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    print(sol.countSubstrings(s)) # 3
    s = "aaa"
    print(sol.countSubstrings(s)) # 6
