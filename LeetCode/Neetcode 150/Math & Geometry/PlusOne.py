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
        - Derive a way of incrementing a list of 
        digits by 1
        - Loop over each digit
        - Add 1 to each digit
        - Maintain a carry in case sum above 9 when 
        adding 1 to a digit
        
        - Problem: Derive a way of incrementing a 
        list of digits by 1
        - Loop from units digit upwards
        - Set carry to zero
        - Add 1 to units digit and update carry
        - For every subsequent digit add 1 if 
        carry is 1, and update carry

        - Problem: Loop over each digit
        - Use a for loop
        
        - Add 1 to each digit
        - Maintain a carry in case sum above 9 when 
        adding 1 to a digit

        - O(n) time <- checking each digit in list
        - O(1) space <- no extra space is needed 
        except carry
        '''

        # Reverse the digits array
        digits = digits[::-1]

        # Keep track of carry and index of position 
        # of digits we are at
        one, i = 1, 0

        while one == 1:
            
            if i <len(digits):
                if digits[i] == 9:
                    # We get the carry case!
                    one = 1
                    # Set to zero
                    digits[i] = 0
                else:
                    # The digit is not 9
                    # Increment this by 1
                    digits[i]+=1
                    # Take carry back down to 
                    # zero
                    one = 0
            else:
                # We are out of bounds

                # Append 1 to end of reverse list
                digits.append(1)

                # Now we don't have a 1, set it 
                # back to zero
                one = 0
            # Increment our index
            i+=1
        
        # Undo reversal and return it
        return digits[::-1]

if __name__ == "__main__":
    sol = Solution()
    digits = [1,2,3,4]
    print(sol.plusOne(digits)) # [1,2,3,5]
    sol = Solution()
    digits = [9,9,9]
    print(sol.plusOne(digits)) # [1,0,0,0]