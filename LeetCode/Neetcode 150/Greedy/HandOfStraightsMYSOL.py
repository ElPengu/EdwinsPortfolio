class Solution:
    def isNStraightHand(self, hand, groupSize):
        '''
        - hand[i] is value on the ith card
        - Integer groupSize
        - We want to rearrange the cards into groups
        - Each group must be of size groupSize
        - The card values in each group must 
        increase by 1 consecutively
        - Return true if this is possible

        - Hm
        - In a greedy way, you kind of want a circuit
        - So if you see 1,2,3,4,5,6,7 that's fine
        - If you see 3,4,5,6,7,1,2 that is also fine
        - Putting groupSize aside for the moment

        - First check: len(hand)%groupSize == 0
        -> Otherwise it is impossible to even 
        create the groups

        - Bruh I clicked an accidentally saw "heap"
        - Of course!
        - Just heapify the hand in O(n) time
        - Then pop... WAIT
        - What about duplicates?!
        - You could throw duplicates into a ... 
        set?
        - FAAAACK, idk
        - When we see a duplicate... we want to see 
        if will be used in the next hand
        - WAIT
        - Duplicates will still be popped IN ORDER 
        - How can we take advantage of this...
        - If we read 1,2,3,4,5 then that's obvious
        - If we read 1,1,2,2,3,3,4,4,5,5, just wait 
        for the next pair
        - What if we read 1,2,2,3,3,4,4,5,5,6?
        - I don't know
        '''

        pass

if __name__ == "__main__":
    sol = Solution()
    hand = [1,2,4,2,3,5,3,4]
    groupSize = 4
    print(sol.isNStraightHand) # True
    hand = [1,2,3,3,4,5,6,7]
    groupSize = 4
    print(sol.isNStraightHand) # False
