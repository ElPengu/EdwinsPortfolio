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

        - It is very useful to understand this problem
        - s = "eccbbbbdec"
        - So let's focus on the first 'e'
        - As soon as we see the second 'e', we will 
        have the substring such that letter 'e' 
        does NOT 
        appear outside outside the substring 
        - However, we want a substring such that 
        *every* letter in it does not appear outside 
        of the substring, we still need to get 'c'
        - Therefore the length of the substring is 
        10, there are no other substrings

        - We will generate a hash map to find out 
        the last index that a character appears in
        - letter->lastIndex
        - O(n) time <- to loop over s
        - O(1) space <- 26 Latin characters

        - Let us maintain an output array to store 
        subarray sizes
        - It is helpful to maintain the size of the 
        CURRENT partition
        - Finally, we will maintain end, for the end 
        of the partition as far as we know SO FAR
        -> Use example s = "eccbbbbdec"
        -> When we see letter e, we assume that the 
        sublist will end at index 8
        -> But then we see letter c, so we now 
        assume that the sublist will end at index 9 
        -> Now we see letter c, then d, which don't 
        tell us that the final index of the 
        partition will be any farther that we 
        currently assume 
        
        - As we search for the end we increment size, 
        updating end as necessary
        - As soon as we land on end pointer we add 
        size to output and reset size to zero
        -> Don't worry, end pointer will update 
        automatically when we see the next element 
        should it exist  

        - 20 minutes 2 minutes for this!!!
        '''

        # Build our hash map
        # letter -> last index in s
        lastIndex = {}

        for i, c in enumerate(s):
            # As we carry on through s, we 
            # will now have letter c mapped 
            # to the index at the  LATEST 
            # time that we saw it in s  
            lastIndex[c] = i

        # For the size of each partition
        res = []
        # Maintain the size we are seeing, and 
        # the end that we are searching for
        size, end = 0, 0

        for i, c in enumerate(s):
            # We add the character to the parition
            size += 1
            # Update end to be as far at the last 
            # index for the character that we are 
            # at
            end = max(end, lastIndex[c])

            if i == end:
                # We have the size of the current 
                # partition
                res.append(size)

                # Reset size for the next partition 
                # that we may create
                size = 0
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "xyxxyzbzbbisl"
    print(sol.partitionLabels(s)) # [5, 5, 1, 1, 1]
    s = "abcabc"
    print(sol.partitionLabels(s)) # [6]