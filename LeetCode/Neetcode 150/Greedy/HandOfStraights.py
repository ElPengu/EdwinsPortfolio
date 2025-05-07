import heapq

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

        - E.g., 1,2,3 would be valid but 1,2,4 
        is not

        - Immediately confirm that there is no 
        remainder from dividing hand by groupSize

        - First thing to notice is that there is 
        always a minimum in a hand. Let's say 
        that it is i
        - i must be the minimum of its group!
        
        - A convenience thing that we will do 
        is count the number of copies that a 
        card has for ease, using a hash map
        - Let count be the hash map
        - count[i]=copies of card with value i

        - We will find the minimum in the hash 
        map and then create a group by finding 
        its successors in the hash map
        - Each time that you use a card you 
        must decrement the count
        - O(1) time for hash map

        - After this, you find the next minimum
        - How do you find these minimum values 
        in better than O(n) time?
        - We will use a minHeap to store all 
        the card values!
        - Once a count hits zero in the hash map, 
        we can pop it from the heap
        - O(n) time for heapify
        - O(n log n) time for popping every card 
        value

        - What if we try to pop the card with 
        value i from the MinHeap but see a 
        card with value j<i?
        - Then card j must be the minimum of 
        the group that we are trying to create
        - We have accessed card i so we must 
        be trying to put it in the same group 
        as card j
        - Card j will still be waiting to be 
        put in a group with now non-existent 
        cards i
        - Therefore we cannot create a hand 
        for this card j!
        '''

        if len(hand)%groupSize:
            # Check whether we can even break the cards
            return False

        # We create a hash map to keep count of all 
        # the cards available to us
        count = {}
        for n in hand:
            # Increment the count of cards with value 
            # count[n]
            count[n] = 1 + count.get(n,0)

        # Create a list of the keys in the hash map
        minH = list(count.keys())
        # Heapify!
        heapq.heapify(minH)

        while minH:
            # We keep on selecting the minimum in 
            # the heap

            # Get the minimum
            first = minH[0]

            for i in range(first, first + groupSize):
                # We work from this value to the groupSize

                # Is this value even in the count dictionary?
                if i not in count:
                    # If we cannot select this card, then 
                    # we cannot create this group!
                    return False
                # Use the card
                count[i]-=1
                if count[i] == 0:
                    # Is the count for this card zero now?
                    if i != minH[0]:
                        # The count for card i is zero, but the 
                        # minimum of the group that we are 
                        # making is NOT card i
                        # Therefore, when we try to create the 
                        # NEXT group with the current minimum, 
                        # card i will not be available
                        # Therefore we return False!

                        return False
                    # We have totally used the card with 
                    # minimum value to create all possible groups!
                    # Now we pop this card and move on to the 
                    # next one
                    heapq.heappop(minH)
        # We created all the groups!
        return True
        pass

if __name__ == "__main__":
    sol = Solution()
    hand = [1,2,4,2,3,5,3,4]
    groupSize = 4
    print(sol.isNStraightHand(hand,groupSize)) # True
    hand = [1,2,3,3,4,5,6,7]
    groupSize = 4
    print(sol.isNStraightHand(hand,groupSize)) # False
