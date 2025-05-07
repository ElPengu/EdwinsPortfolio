from typing import List
from collections import defaultdict
import heapq

class Twitter:
    # This is quite an involved design problem!
    # This is even harder than the merge K sorted list problem!
    # 
    # We will consider follow and unfollow as a pair of related 
    # functions, and postTweet and getNewsFeed as pairs of related 
    # functions
    # 
    # For follow and unfollow
    # We COULD naively use a hash map follower -> list of followee IDs 
    # for follow function
    # But the unfollow function becomes an O(n) operation. Can 
    # we do better?
    # Yes!
    # We will use a hash map followeeID -> HASH SET of follower IDs
    # Now unfollow is O(1) operation
    # 
    # For postTweet and getNewsFeed
    # Let us naively consider hash map userID->list of tweet ID for 
    # postTweet. Adding is O(1) time. This may work
    # getNewsFeed is quite difficult
    # Example: A user can follow users 1 and 2, with tweet ids [1,2,3] 
    # and [4,5,6]. Let 3 and 6 be the latest for users 1 and 2 
    # respectively. Which one is the absolute latest?
    # To answer this, let us go back to the postTweet function, and we 
    # will update our hashMap for postTweet to be userID->list of [count, TweetID]
    # Now we return to getNewsFeed
    # We take our user ID and get the HASH SET of followee IDs (from 
    # follow/unfollow)
    # This corresponds to our list of userIDs, which we can use 
    # to get a list of [count, TweetID] for each
    # We will now "merge" these lists!
    # We now put a pointer at the *frontier* (latest tweet id) of each  
    # list, then create a heap of tweets  across each list to a heap in O(k)
    # time.
    # Finally, we select the minimum in O(1) time.
    # Repeat this 10 times to achieve O(10*k) time, but at least 
    # extracting the minimum value is O(10*log k) time total
    # Each time we POP with getNewsFeed, so how can we update
    # the heap so that we don't run out of the 10 latest tweets?
    # Now this is a bit convoluted
    # We will store FOUR items: count, tweetId, followeeId, index-1
    # Where index is for that followee's particular tweets
    # The minHeap works on the latest count
    # We pop, and we can add the tweetId to the result
    # Next, we check if index-1>=0. If so, that user has some earlier
    # tweets
    # index-1>=0 -> push [count, tweetId, followeeId, index-1] onto the
    # heap!
    # 
    #



    def __init__(self):
        # timer
        self.count = 0 
        # userID -> list of [count, tweetIDs]
        self.tweetMap = defaultdict(list)
        # userID -> set of followeeIDs
        self.followMap = defaultdict(set) 
        

    def postTweet(self, userId: int, tweetId: int)->None:
        # We must add a pair of count (for time) and tweetId
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement count. We want the minimum heap to pop
        # the latest tweet. Therefore, we must decrement
        # the count to account for this.
        self.count-=1


    def getNewsFeed(self, userId: int)->List[int]:
        # We will have a list of tweets from most recent
        res = []
        # To figure out the most recent we use a min heap
        minHeap = []

        # A user follows himmself
        self.followMap[userId].add(userId)
        # We must loop over the tweets of every followee
        for followeeId in self.followMap[userId]:
            # We want the most recent tweet, the frontier!

            if followeeId in self.tweetMap:
                # If it has at least one tweet
                    
                # Get the last value of the list
                index = len(self.tweetMap[followeeId]) - 1
                # Get pair of values at end of list
                count, tweetId = self.tweetMap[followeeId][index]
                # Append to the min heap. 
                # Count: Use the count as the key. We will also add 
                # the tweetId so that we know the tweet
                # tweetId: added to the result
                # followeeId: to get the new latest tweet from this 
                # user
                # index-1: Next position to look at if it is there
                minHeap.append([count, tweetId, followeeId, index-1])
        
        # Heapify the minHeap <- O(k)
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            # Pop the four values
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # Append the latest tweet
            res.append(tweetId)

            # Assuming that there are more unread tweets
            if index >= 0:
                # Now we push the latest unread tweet for the followee
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])

        return res

    def follow(self, followerId: int, followeeId: int)->None:
        # Just add the new followee to the set for the follower!
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int)->None:
        # We check if the user follows the followee
        if followeeId in self.followMap[followerId]:
            # Remove the id
            self.followMap[followerId].remove(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    print(twitter.postTweet(1, 10)) # User 1 posts a new tweet with id = 10.
    print(twitter.postTweet(2, 20)) # User 2 posts a new tweet with id = 20.
    print(twitter.getNewsFeed(1))   # User 1's news feed should only contain their own tweets -> [10].
    print(twitter.getNewsFeed(2))   # User 2's news feed should only contain their own tweets -> [20].
    print(twitter.follow(1, 2))     # User 1 follows user 2.
    print(twitter.getNewsFeed(1))   # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
    print(twitter.getNewsFeed(2))   # User 2's news feed should still only contain their own tweets -> [20].
    print(twitter.unfollow(1, 2))   # User 1 follows user 2.
    print(twitter.getNewsFeed(1))   # User 1's news feed should only contain their own tweets -> [10].