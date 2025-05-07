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
        - Multiplying two numbers like in school
        - Multiplying a single digit out of a 
        multi-digit numbers with another numbers
        - Combining the results after multipling 
        each digit of one number with the entirety 
        of the other number
        - Coding up solution to multiplying two 
        numbers
        - Finding the maximum number of digits 
        possible from multipling num1 of length N 
        by num2 of length M

        - Example throughout: 123*456

        - Problem: Multiplying two numbers like in 
        school
        - Consider 123*456
        - You would do 6*123, 5*123, and 4*123 and 
        combine the solutions

        - Problem: Multiplying a single digit out 
        of a multi-digit numbers with another 
        numbers
        - Consider 6*123
        - You start at index 0
        - You would find 6*3=18
        - Traditionally you would store 18%10(=8) 
        in the result and use the 18//10(=1) as a 
        carry
        - To make this easy to code we will store 
        18%10 as the number in index 1
        - res=81
        - Move to the next index, which holds 1 
        -> In the code index would be 1
        - You find 6*2=12
        - You add 12%10(=2) to what is at index 1, 
        and store 12//10(=1) at the next index
        - res = 831
        - Move to the next index, which holds 1
        -> In the code index would be 2
        - You find 6*1=6
        - You add 6%10(=6) to what is at index 2, 
        and store 12//10(=0) At the next index
        - res = 8370
        - We remove the trailing zero, as it would 
        be a leading zero in the actual solution
        - res = 837
        - Reverse digits in res
        - res = 738 = 6*123

        - Problem: Combining the results after 
        multiplying each digit of one number with 
        the entirety of the other number
        - Consider 123*456
        - Assume that you can find the results for 
        6*123, 5*123, and 4*123
        - Set index i = 0 
        - You first find 6*123 and store it, 
        unreversed and with all trailing zeroes
        - Now you increment to index i=i+1=2
        - As you would find 5*123, find the result 
        after 5*3
        - Add ((5 * 3)//10) to whatever is in j=i=1, 
        and add (( 5* 3)%10) to whatever is in j+1=2 
        - Move to j=j+1=2
        - Find the result after 5 * 2
        - Add ((5*2)//10) to whatever is in j=2, 
        and add ((5*2)%10) to whatever is in j+1=3
        - Move to j=j+1=3
        - Find the result after 5 * 1
        - Add ((5*1)//10) to whatever is in j=3, 
        and add ((5*1)%10) to whatever is in j+1=4
        - Repeat this from i=i+1=2 for 4*123

        - Problem: Coding up solution to multiplying two 
        numbers
        - We will pre-allocate the output array of 
        integers
        - Luckily, we know maximum size of the array
        - When performing multiplication operations 
        on the digits we will start from the right 
        -> This allows us to read them in reverse 
        order 
        - When combining the solutions to the 
        single-digit multiplications, the result 
        would be built in reverse order
        - Therefore we will start storing the result 
        from the FIRST INDEX of the output array
        - Return the output array into a string 
        without any potential empty elements at 
        the end
        -> The empty elements can be treated as 
        trailing zeroes

        - Problem: Finding the maximum number of 
        digits possible from multiplying num1 of 
        length N by num2 of length M
        - If num1 has N digits, it is between 
        10^(N-1) and (10^N)-1
        - If num2 has M digits, it is between 
        10^(M-1) and (10^M)-1
        - Maximum value of num1*num2 strictly 
        speaking is 
        (10^(N-1)) * (10^(M-1)) = 10^(N+M-2)
        - We can upper bound this to 
        (10^N) * (10^M) = 10^(N+M)
        - If a number has N+M digits, it is at most 
        10^(N+M)
        - Therefore the upper bound for the number 
        of digits is N+M


        - O(m ∗ n) time <- Every digit in num1 
        is multiplied with every digit in num2
        - O(m + n) space <- You can prove that 
        given two numbers have number of digits M 
        and N respectively, the number of digits in 
        its product will be M + N 
        '''     

        # Trivial case
        if "0" in [num1,num2]:
            return "0"

        # Create result
        res = [0]*(len(num1)+len(num2))

        # Reverse both lists
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            # num1 is treated as the single-digit 
            # number as in the explanation

            # Therefore i1 points to the START index 
            # for combining the multiples

            for i2 in range(len(num2)):
                # num2 is treated at the multi-
                # digit number as in the 
                # explanation    
                
                # Due to the definition of i1, we 
                # are always adding the result of 
                # multiplying to the START INDEX 
                # (i1) sum the CURRENT INDEX in 
                # num2 (i2)
                # i1+i2

                # The carry therefore is stored in 
                # the index following i1+i2
                # i1+i2+1

                # Take the digits from each numbers 
                # and multiply them
                digit = int(num1[i1])*int(num2[i2])

                # Initially add "digit" to what 
                # is in i1+i2
                # This makes finding the carry easier
                res[i1+i2]+=digit
                # Put the carry into the next 
                # position
                res[i1+i2+1] += (digit//10)
                # After dealing with the carry, 
                # ensure that only the units part 
                # of digit is stored
                res[i1+i2]=res[i1+i2]%10

        # Reverse the result
        res, beg = res[::-1], 0

        # Remove trailing zeroes
        while beg < len(res) and res[beg] == 0:
            beg+=1

        # Convert every integer to a string
        res = map(str, res[beg:])

        # Return the list as a string
        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    num1 = "3"
    num2 = "4"
    print(sol.multiply(num1,num2)) #12
    
    num1 = "111"
    num2 = "222"
    print(sol.multiply(num1,num2)) #24642