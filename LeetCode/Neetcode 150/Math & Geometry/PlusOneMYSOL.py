from typing import List

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        - You are given array digits
        - digits[i] is ith digit
        - [1,2,3,4] = 1234
        - There will not be a leading zero
        - Return the digits of the integer after 
        incrementing by 1

        - Problems
        - Derive the number represented by digits
        - Increment the number by 1
        - Return the digits derived from this 
        number 

        - Problem: Derive the number represented by 
        digits
        - Set num using list comprehension
        
        - Problem: Increment the number by 1
        - Increment num

        - Problem: Return the digits derived from 
        this number 
        - Set numDigits using list comprehension
        - Return numDigits

        '''

        # Set variables for number and digits of it 
        num = ""
        numDigits = None

        # Derive the number represented by digits
        for d in digits: num+=str(d)        
        num = "".join(num)
        num = int(num)
        # Increment the number by 1
        num += 1 
        
        # Return the digits derived from this 
        # number
        numDigits = [i for i in str(num)] 
        return numDigits

if __name__ == "__main__":
    sol = Solution()
    digits = [1,2,3,4]
    print(sol.plusOne(digits)) # [1,2,3,5]
    sol = Solution()
    digits = [9,9,9]
    print(sol.plusOne(digits)) # [1,0,0,0]