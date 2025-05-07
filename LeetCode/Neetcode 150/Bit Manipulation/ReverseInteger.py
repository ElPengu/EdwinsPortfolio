import math

class Solution:
    def reverse(self, x: int) -> int:
        '''
        - You are given a signed 32-bit integer x
        - Return x after reversing each of its 
        digits
        - After reversing, if x goes outside the 
        signed 32-bit integer range [-2^31,2^31 -1] 
        then return 0 instead
        - Solve the problem without using integers 
        that are outside the signed 32-bit integer 
        range

        - Problems
        - Reversing any integer
        - Only using integers within the signed 
        32-bit integer range WITHOUT building the 
        number
        
        - Reversing any integer
        - Take x and mod it by 10, this gets 
        remainder r
        - Add r to res
        - Floor divide x by 10
        - If x remains, then multiply res by 10
        - Repeat, but now ADD r to res

        - Only using integers within the signed 
        32-bit integer range WITHOUT building the 
        number
        - We explicitly look at our max and min
        - MAX =  2147483647
        - MIN = -2147483648
        - MAX and MIN have 10 digits
        - As we build our reverse, we will keep on 
        adding digits
        - Once we hit 9 digits in res, we must make 
        some checks before adding the next digit
        - We check how res relates to MAX//10 and 
        MIN//10
        - If we see that res > MAX//10 or res < 
        MIN//10 then we certainly cannot add 
        another digit
        - If we see that res == MAX//10 or res == 
        MIN//10 then check if digit >= MAX%10 or 
        digit <= MIN%10 respectively
        -> We certainly cannot add another digit 
        in this case!
        '''

        # Integer.MAX_VALUE =  2147483647 (ends 7)
        # INTEGER.MIN_VALUE = -2147483648 (ends -8)

        MIN = -2147483648
        MAX = 2147483647

        res=0
        while x:
            # Continue until x is 0

            # Python thinks that -1%10=9
            digit = int(math.fmod(x,10))
            # Python thinks that -1//10=-1
            x = int(x/10)

            if (res > MAX//10 or 
                (res == MAX//10 and digit >= MAX % 10)):
                # If we exceed the prefix to the 
                # final digit of MAX, then we 
                # will exceed
                # If we are exactly equal to that 
                # prefix AND the digit we will add 
                # exceed the final digit of MAX, 
                # then we will overflow!
                return 0
            if (res < MIN//10 or 
                (res == MIN//10 and digit <= MIN % 10)):
                # If we are less than the prefix to 
                # the final digit of MIN, then we 
                # will exceed
                # If we are exactly equal to that 
                # prefix AND the digit we will add 
                # exceed the final digit of MIN, 
                # then we will overflow!
                return 0 

            # We can add the digit to res!

            res = (res*10)+digit 

        return res

if __name__ == "__main__":
    sol = Solution()
    x = 1234
    print(sol.reverse(x)) # 4321
    sol = Solution()
    x = -1234
    print(sol.reverse(x)) # -4321
    x = 1234236467
    print(sol.reverse(x)) # 0