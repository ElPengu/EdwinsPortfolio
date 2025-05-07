class Solution:

    def longestPalindrome(self, s: str) -> str:
        
        '''
        - We want the longest substring that is a 
        palindrome
        - Palindrome: Reads the same forwards and 
        backwards
        - If there are multiple return any ONE of 
        them

        - How could we build this up?
        - A brute force approach would be to start
        at each index and see if you have a 
        palindrome by the final index, then the one 
        before, and so forth

        - Technically, a palindrome can be generated
        by adding the same letter to either side of a
        palindrome
        - What is a "base" palindrome?
        - An empty string of a single character

        - We could do two things
        - First loop over every index in s and try 
        to prepend and append characters whilst the 
        same
        - Next loop over every PAIR of indices in 
        s and try to prepent and append characters
        whilst the same
        
        - Is there repeated work?

        - You might consider the same character n times

        - Got this in 20 minutes and it was the 
        correct intuition and working code, wow!!!
        '''

        res = ""

        MININDEX, MAXINDEX = 0, len(s)-1

        for i in range(len(s)):
            palindrome = s[i]
            minIndex, maxIndex = i-1, i+1
            while minIndex >=MININDEX and maxIndex <= MAXINDEX:
                if s[minIndex] == s[maxIndex]:
                    palindrome = s[minIndex] + palindrome + s[maxIndex]
                minIndex-=1
                maxIndex+=1
            if len(palindrome) > len(res): res = palindrome

        for i in range(len(s)-1):
            j = i+1
            if not s[i] == s[j]: continue
            palindrome = s[i]+s[j]
            minIndex, maxIndex = i-1,j+1
            while minIndex >=MININDEX and maxIndex <= MAXINDEX:
                if s[minIndex] == s[maxIndex]:
                    palindrome = s[minIndex] + palindrome + s[maxIndex]
                minIndex-=1
                maxIndex+=1
            if len(palindrome) > len(res): res = palindrome
        
        return res



if __name__ == "__main__":
    sol = Solution()
    s = "ababd"
    print(sol.longestPalindrome(s)) # "bab" or "aba"
    s = "abbc"
    print(sol.longestPalindrome(s)) # "bb"