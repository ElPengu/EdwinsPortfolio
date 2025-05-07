class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # This is the same in concept as my solution, 
        # just a LOT more cleaner
        # If s has length 0 or is smaller than t, return ""
        # We have a left and right pointer. Also optimals
        # Left points to the start of the substring
        # Right points to the character that WILL BE added
        # We have a hash map for the window we HAVE: {char: count}
        # We have a hash map for the window we NEED: {char: count}
        # Set matches = 0
        # The NEED hash map only counts the characters in t
        # For every character we add, we compare if the count 
        # for the character added to HAVE == in NEED
        # For every character we remove, we compare if the count 
        # that we removed from HAVE+1 == in NEED. If so, decrement
        # matches
        # See how matches only changes if the condition changes. We 
        # only change ONCE the >= condition is met or broken. 
        #
        # Finally, if matches == len(t), we increment left, else 
        # we increment right
        #
        # Loop until both pointers are at the end
        
        # We return empty string if t is empty
        if t == "":
            return ""

        # We set two windows. One for string t, and for the window
        # Only the window will be updated
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # We set have to zero because there are no characters yet in 
        # the window to match with t
        # We need exactly as many characters as there are in the 
        # set of t to match wih the window
        have, need = 0, len(countT)

        # Result will be a pair of pointers for the window
        # The length of res is initially infinite
        res, resLen = [-1, -1], float("infinity")

        # Left pointer is at 0
        l = 0
        # We increment the right pointer
        for r in range(len(s)):
            # We add the character at r to the window
            c = s[r]

            # We update the hash map for the window 
            # to have one more occurence of the character 
            # that r is pointing to
            window[c] = 1 + window.get(c, 0)

            # In the case that the frequencies in 
            # both the window and t match, we 
            # have one more matching character so 
            # we increment our have count
            # Note that we only care about characters 
            # in string t
            if c in countT and window[c] == countT[c]:
                have += 1

            # When we get to the point that have == need, 
            # we know that the characters in t occur at the 
            # same frequency as in the window. We try 
            # to shorten the window
            while have == need:
                if (r - l + 1) < resLen:
                    # We must update the optimal window 
                    # and the resulting length if 
                    # it is smaller than our best result 
                    # length so far
                    res = [l, r]
                    resLen = r - l + 1
                    
                # We continuously make the window smaller 
                # from the left
                # So the frequency of this character 
                # in the window will shrink
                window[s[l]] -= 1
                
                # We must check if our have is still the same
                # Again, we only care if the character is in 
                # t
                # Critically, if we get to the point where 
                # the count is now SMALLER in the window, then 
                # we know that we have lost a matching character
                # 
                # Note that the second condition will be false 
                # if have == need, AND will only occur once, 
                # right after this the while condition will not 
                # hold!
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        # We set l and r pointers to be whatever res is
        l, r = res

        # We return the string that l and r point to 
        # unless they have not changed at all
        return s[l : r + 1] if resLen != float("infinity") else ""

if __name__ == "__main__":
    sol = Solution()
    s = "OUZODYXAZV"
    t = "XYZ"
    print(sol.minWindow(s,t)) # "YXAZ"
    s = "xyz"
    t = "xyz"
    print(sol.minWindow(s,t)) # "xyz"
    s = "x"
    t = "xy"
    print(sol.minWindow(s,t)) # ""