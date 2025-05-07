class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Set two pointers, left and right
        #Left pointer at start, right at end
        #While a pointer is not pointing to an alphanumeric
        #character, move inwards
        #Make checks whilst left < right

        #Set pointers
        left, right = 0, len(s)-1
        
        #Whilst left is less than right
        while left < right:
            #Increment left until it points to an alpha-numeric character
            while s[left].isalnum() == False:
                left+=1
            #Decrement right until it points to an alpha-numeric character
            while s[right].isalnum() == False:
                right-=1

            #Check whether they are equal. Use lower in case a character 
            #is in upper-case
            if s[left].lower() != s[right].lower():
                return False
            
            #Increment left and decrement right
            left += 1
            right -= 1
            
        #Palindrome verified
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "Was it a car or a cat I saw?"
    print(sol.isPalindrome(s)) # True
    s = "tab a cat"
    print(sol.isPalindrome(s)) # False