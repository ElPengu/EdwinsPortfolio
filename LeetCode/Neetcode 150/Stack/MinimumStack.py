class MinStack:
    
    def __init__(self):
        # Two stacks

        # This is the regular stack
        self.stackArray = []
        # This stack stores at index i 
        # the minimum element that is in 
        # the array AT index i 
        # in the stack array 
        self.minStackArray = []

    def push(self, val:int) -> None:
        self.stackArray.append(val)

        if len(self.minStackArray) == 0:
            #If the minimum stack is empty, add the val
            self.minStackArray.append(val)
        else:
            # We append the minimum of the last added to 
            # the minimum stack and this val
            self.minStackArray.append(min(self.minStackArray[-1], val))
        
    def pop(self) -> None:
        
        self.stackArray.pop(-1)

        
        # We pop the minimum added to the minStackArray
        self.minStackArray.pop(-1)


    def top(self) -> int:
        return self.stackArray[-1]
    
    def getMin(self) -> int:
        # Since the minimum stack array holds all minimum values added 
        # to the stack since THAT value was added, we just return this 
        # value
        return self.minStackArray[-1]


if __name__ == "__main__":
    minStack = MinStack();
    print(minStack.push(1));
    print(minStack.push(2));
    print(minStack.push(0));
    print(minStack.getMin()); # return 0
    print(minStack.pop());
    print(minStack.top());    #// return 2
    print(minStack.getMin()); #// return 1
