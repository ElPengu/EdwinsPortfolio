class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        '''
        - num1 and num2 are non-negative integers
        - Return product of num1 and num2 as a 
        string
        - Assume no leading 0, unless they are the 
        number 0 itself
        - Do not use an built-in library to convert 
        inputs into integers

        - Problems
        - Perform multiplication across two digits
        - Return the result as a string

        - Problem: Perform multiplication across 
        two digits
        - Initialise carry = 0
        - Our base case is the first two digits
        - Multiply them
        - Store result//10
        - Set carry = result%10
        - Inductive step
        - Multiply two digits, add carry to result
        - Store result//10
        - Set carry = result%10 as before

        - Problem: Return the result as a string
        - Set string res to be empty
        - Update res in the while loop for the 
        multiplication

        - DAMN, I FORGOT THAT MULTIPLICATION 
        DOESN'T ADD COLUMN BY COLUMN LIKE IN 
        ADDITION!!!
        '''
        # Set res as empty string
        res = ""
        # Initialise carry
        carry = 0
        # Set pointers for num1 and num2
        i, j = 0, 0

        # Reverse num1 and num2 because I am lazy
        num1 = num1[::-1]
        num2 = num2[::-1]
        print(f"10%10=0: {10%10}")
        print(f"10//10=1: {10//10}")
        # Perform multiplication across two digits
        while (i < len(num1) or j < len(num2)):

            # Find the product of multiplication
            product = int(num1[i])*int(num2[j])
            # Add carry to product
            product += carry
            # Append units digit of product to 
            # res
            res+=str(product%10)
            # Set carry to tens digit of 
            # product
            carry = product//10

            # Update pointers
            i+=1
            j+=1

        # In case one number is longer than the 
        # other

        while (i<len(num1)):
            # num1 has digits remaining
            # Set product
            product = int(num1[i])
            # Add carry to product
            product+=carry

            # Append units digit of product to 
            # res
            res+=str(product%10)
            # Set carry to tens digit of product
            carry = product//10

            # Update pointer
            i+=1

        while (j<len(num2)):
            # num2 has digits remaining
            # Set product
            product = int(num2[j])
            # Add carry to product
            product+=carry

            # Append units digit of product to 
            # res
            res+=str(product%10)
            # Set carry to tens digit of product
            carry = product//10

            # Update pointer
            j+=1

        # In case of extra carry
        res+='1'

        # Due to reversing num1 and num2, then 
        # appending, we must reverse 

        # Return the result as a string
        return res[::-1]


if __name__ == "__main__":
    sol = Solution()
    num1 = "3"
    num2 = "4"
    print(sol.multiply(num1,num2)) #12
    
    num1 = "111"
    num2 = "222"
    print(sol.multiply(num1,num2)) #24642