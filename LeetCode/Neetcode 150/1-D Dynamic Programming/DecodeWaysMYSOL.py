class Solution:

    def numDecodings(self, s: str) -> int:

        '''
        - 'A'->"1", 'B'->"2", ..., 'Z'->"26"
        - The message 1012 can be decoded like this
        -> "JAB" -> (10 1 2)
        -> "JL" -> (10 12)
        
        - Find the number of ways to decode a 
        message

        - Let's abstract the mapping 
        number string->character
        
        - We know that a string can be at most TWO
        characters
        - If a string is TWO characters and starts
        with anything except a 1 then it is invalid

        - We can start at the end index and work backwards
        - Index N will always be at most one way
        - Index N-1 may be one or two ways. If it is a 1 it 
        is two ways, else one way
        
        - BASE CASE: Last index has 1 way
        - INDUCTIVE CASE: 
        -> IF NOT '1': ways += 0
        -> ELSE: ways +=1

        - WAIT! '0' cannot be mapped!!!
        - If '0' is NOT preceded by a 1 then there are 0 ways
        - BASE CASE: IF NOT '0': Last index has 1 way, ELSE 0 ways
        - INDUCTIVE CASE:
        -> IF NOT '1' AND '0' was seen before: return 0
        -> IF NOT '1': ways += 0
        -> ELSE: ways +=1
        - IF '0' last seen: RETURN 0
        - RETURN ways
        '''

        if len(s) == 1:
            # If we have a string of length 1
            if s[0] == '0': return 0
            else: return 1

        # Count for decodings
        res = 0

        # Flags if we have just seen a 0
        flag = 0

        # BASE CASE
        if s[len(s)-1] != '0':
            res+=1
        else:
            res+=0
            # Seen a 0
            flag = 1

        for i in range(len(s)-2,-1,-1):
            # Start from the second-to-last index and work up
            if s[i] != '1' and flag == 1: return 0
            if s[i] != '1': res+=0
            else: res+=1

            if s[i] == '0': flag = 1

        if flag == 1:
            return 0
        return res

        

if __name__ == "__main__":
    sol = Solution()
    s = "12"
    print(sol.numDecodings(s)) # 2
    s = "01"
    print(sol.numDecodings(s)) # 0