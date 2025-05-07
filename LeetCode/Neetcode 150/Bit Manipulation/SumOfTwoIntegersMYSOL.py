
class Solution:

    def getSum(self, a: int, b: int) -> int:
        '''
        - Integers a and b
        - Return the SUM of the two integers
        - Do not use + or -

        - Let's leave negatives for a minute

        - Given positive integers a and b, let's 
        represent them in binary

        - In binary addition, you need a carry
        - I want the following operations
        - 0 * 0 => 0
        - 0 * 1 => 1
        - 1 * 0 => 1
        - 1 * 1 => 0
        - This is XOR
        - 0^0=>0
        - 0^1=>1
        - 1^0=>1
        - 1^1=>0
        - I want to set carry to 1 when doing 1 * 1
        - IF x&y == 1: carry=1
        
        - Those are the basics
        - How do we incorporate carry into this 
        though?
        - Case 1: carry flag is off
        - Place the result as it
        - Case 2: carry flag is on
        - If result is 0, set it to 1 and set carry 
        flag off
        - If result is 1, set result to 0 and set 
        carry flag on

        - How do we go bit by bit?
        - Start with the LSB using modulo on a 
        and b each time

        - How do we place the ith bit in the ith 
        position
        - Left bit shift our result i times
        - Set sum = sum | result

        '''        

        sum = 0
        carry = 0
        i = 0
        while a and b:
            # Consider all of a and b

            # The bit that we will add
            res = 0

            # Get the LSB of a and b
            bitA = a%2
            bitB = b%2

            # Set res using bits
            res = bitA^bitB
            
            res = res&carry

            carry = 0

            # Update sum
            sum = sum | (res << i)

            # Right shift a and b
            a = a>>1
            b = b>>1

            i+=1

        while a:
            # Consider all of a and b

            # The bit that we will add
            res = 0

            # Get the LSB of a and b
            bitA = a%2

            # Set res using bits
            res = bitA

            res = res&carry

            carry = 0

            # Update sum
            sum = sum | (res << i)

            # Right shift a
            a = a>>1

            i+=1

        while b: 
            # Consider all of a and b

            # The bit that we will add
            res = 0

            # Get the LSB of b
            bitB = b%2

            # Set res using bits
            res = bitB

            res = res&carry

            carry = 0

            # Update sum
            sum = sum | (res << i)

            # Right shift b
            b = b>>1

            i+=1

        return sum

if __name__ == "__main__":
    sol = Solution()
    a = 1
    b = 1
    print(sol.getSum(a,b)) # 2
    a=4
    b=7
    print(sol.getSum(a,b)) # 11