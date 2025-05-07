class Solution:

    def isValid(self, s: str)-> bool:
        # We need a stack like way of reading this
        # Initialise a stackArray
        # Every time you add an opening character, do so
        # Every time you add a closing character, 
        # compare it with the character at the start of the array
        # If they correspond, REMOVE the start character
        # NOTE that if there is no start character, return false
        # Return the truth value len(stackArray) == 0
        # For ease of use we create a hash map for checking 
        # corresponding characters as well as an opening char 
        # set and a closing char set

        # 1. Initialise stackArray
        stackArray = []

        # 2. For ease of checking, create a correspondsHashMap
        correspondsHashMap = {}
        correspondsHashMap[')'] = '('
        correspondsHashMap['}'] = '{'
        correspondsHashMap[']'] = '['

        # 3. For easy of use create an opening character set 
        # and a closing character set
        openCharSet = set()
        openCharSet.add('(')
        openCharSet.add('{')
        openCharSet.add('[')
        closedCharSet = set()
        closedCharSet.add(')')
        closedCharSet.add('}')
        closedCharSet.add(']')

        # 3. Iterate over s
        for c in s:
            # If this is an opening character, add it immediately
            if c in openCharSet:
                stackArray.append(c)
            elif c in closedCharSet:
                # We are dealing with a closed character
                if len(stackArray) == 0:
                    # In the case that this is a starting character 
                    # for the stack, we immediately return false
                    return False
                else:
                    # Does the last character in the stack correspond?
                    if stackArray[-1] == correspondsHashMap[c]:
                        #We must remove the first element
                        stackArray.pop(-1)
                    else:
                        return False
                
            else:
                #We have an invalid character
                return False

        # 4. Return whether the stack is empty
        return len(stackArray) == 0

        pass


if __name__ == "__main__":
    sol = Solution()
    s = "[]"
    print(sol.isValid(s)) # true
    s = "([{}])"
    print(sol.isValid(s)) # true
    s = "[(])"
    print(sol.isValid(s)) # false