class TimeMap:
    # Data structure
    # For get() to work, we need to have a sorted list of keys by 
    # time stamp. Luckily we are guaranteed that get() will be 
    # called on time increasing order lists
    # For set()
    # 
    # We will have a hash map. Key is key, value is a <time val> pair
    # 


    def __init__(self):
        # Initialise a store hash map
        self.store = {} # {key: [value, timestamp]}
        pass

    def set(self, key: str, value: str, timestamp: int)-> None:
        # Stores key with value at the timestamp
        if key not in self.store:
            # Create an empty list
            self.store[key] = [] # We could use default dict instead
        #Append to the end of the list
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int)-> str:
        # Returns the most recent value of key if
        # - set was previously called on it
        # - the most recent timestamp for that key is less
        # than or equal to the given timestamp
        # If none, return "" 
        
        # Initialise result to an empty string
        res = ""
        # Get the list
        values = self.store.get(key, [])

        # Binary search
        l, r = 0, len(values)-1

        # While l <= r
        while l <= r:
            m = l + ((r-l)//2)
            
            if values[m][1] <= timestamp:
                # This is a valid value so far, we set the result 
                # to this
                res = values[m][0]
                # Now we shift left up by 1 more than mid and see 
                # if we can get further loops
                l = m + 1
            else:
                # This is invalid so we do not set result
                
                # We shift right down
                r = m-1
        
        return res

                



if __name__ == "__main__":
    timeMap = TimeMap()
    print(timeMap.set("alice", "happy", 1))  # store the key "alice" and value "happy" along with timestamp = 1.
    print(timeMap.get("alice", 1))           # return "happy"
    print(timeMap.get("alice", 2))           # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
    print(timeMap.set("alice", "sad", 3))    # store the key "alice" and value "sad" along with timestamp = 3.
    print(timeMap.get("alice", 3))           # return "sad"
