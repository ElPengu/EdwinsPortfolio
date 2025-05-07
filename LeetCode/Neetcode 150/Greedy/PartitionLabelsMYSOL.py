from typing import List

class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        '''
        - String s contains lowercase english letters
        - We want to create as many substrings as 
        possible, whilst each letter appears in at most 
        one substring
        - Return a list of integers for the size of the 
        substrings in the order that they appear in the 
        string

        - We need a hash map so that we have a count for 
        each time that we see a letter
        - count: {letter->appearances}

        - As we iterate, every letter seen must be fully 
        exhausted before the substring "closes"
        - We can have a set of open letters,
        - set open: letters
        - When we "open" a new substring, we immediately 
        put every letter we see in set open 
        - Now we decrement count[letter]
        - if count[letter] ==0: remove letter from open
        - When open is empty we have created a substring

        - How do we keep track of the size of the substring
        - Keep two pointers
        - left is where we start the substring
        - right stays with us
        - size of substring is right-left+1

        - 20 minutes 2 minutes for this!!!
        '''

        # Stores our result
        res = []

        # Create count dictionary
        count = {}
        # Populate count dictionary
        for letter in s:
            if letter not in count:
                count[letter] = 0
            count[letter]+=1

        # Set to hold all "open" letters that must 
        # be closed
        open = set()

        # Pointers left and right, initialised to 
        # start index
        left, right = 0, 0

        while right < len(s):
            # For ease of reading, set letter
            letter = s[right]
            # We immediately add the letter 
            # to the set open
            open.add(letter)
            
            # Update count for this letter
            count[letter]-=1

            if count[letter] == 0:
                # We have "closed" this letter, 
                # remove it from open
                open.remove(letter)

            # If open is now empty, we have a 
            # partition!
            # Add the size of the partition to res
            if len(open) == 0:
                res.append(right-left+1)

                # We are starting a new partition, 
                # so update left to be equal to 
                # right FOR THE NEXT ITERATION
                left = right+1

            # Increment right pointer
            right += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "xyxxyzbzbbisl"
    print(sol.partitionLabels(s)) # [5, 5, 1, 1, 1]
    s = "abcabc"
    print(sol.partitionLabels(s)) # [6]