class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        # We know that a window is valid if the difference 
        # between its length and the count of whatever 
        # character we are considering is less than k
        # 
        # We set a left and right pointer
        # We have a hash map recording counts for characters, 
        # initially reset to 0
        # Now for each character we enter a loop
        # While the window is VALID for this character, 
        # we shift r out by 1 and update the map based on 
        # the character we see. l to r determines the length 
        # of the maximum window 
        # While the window is INVALID for this character, 
        # we shift l out by 1 and update the map as before
        
        
        res = 0
        # We create a set of characters in s
        # At most this will be 26
        charSet = set(s)

        # This is O(26) operation
        for c in charSet:
            # Set a left pointer to zero
            # Note that the count is also set to 0
            count, l = 0, 0
            # Now we increment a right pointer from 0
            for r in range(len(s)):
                # We always start by increasing the count 
                # if we see the desired character
                if s[r] == c:
                    count += 1

                # If we ever get to a point 
                # where we have a window that 
                # requires more replacements than possible, 
                # we start shifting the right pointer in
                while (r - l + 1) - count > k:
                    # The count decrements if the left 
                    # pointer goes past the target character
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                # We always have a valid window at this point
                # Just update the result
                res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "XYYX"
    k=2
    print(sol.characterReplacement(s, k)) # 4
    s = "AAABABB"
    k = 1
    print(sol.characterReplacement(s, k)) # 5