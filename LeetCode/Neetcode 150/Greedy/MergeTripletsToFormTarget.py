from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        - 2D array of integer triplets
        - triplets[i] = [ai,bi,ci]
        - Array of integers target = [x,y,z]
        - Goal: obtain the target by doing the following zero or more 
        times
        - Choose two DIFFERENT triples triplet[i] and triplet[j]
        - Set triplet[j]=[max(ai,aj),max(bi,bj),max(ci,cj)]
        - Return True if you can obtain the target

        - Key observation: we want to enlarge smaller 
        values WITHOUT exceeding the target value!
        - Consider target = [2,7,5]
        - If we come across [1,8,4], no matter what, 
        applying the operation on it will be useless 
        as we will exceed the target
        - We will exclude these triplets

        - Okay, now all triplets have values at or 
        less than the targeted values
        - We can put away the operation and ask the 
        three following questions:
        -> Does x appear at index 0 in any triplet?
        -> Does y appear at index 1 in any triplet?
        -> Does z appear at index 2 in any triplet?
        - We can safely apply the operation and not 
        exceed the target, so if we answer yes to 
        these three questions then we are good!
        
        - So we will filter out useless triplets 
        and we will answer the three questions on 
        all good triplets

        - O(n) time <- to iterate over all triplets
        '''

        # Note: good specifically holds the set of 
        # indices where triplet[i]==target[i] AND 
        # NOT triplet[j]>target[i]
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                # Do NOT add this to good
                continue
            for i, v in enumerate(t):
                # We get the index
                # We also get the value of this 
                # triplet
                if v == target[i]:
                    # Add this to the good set, we can get
                    good.add(i)
        return len(good) == 3

        
if __name__ == "__main__":
    sol = Solution()
    triplets = [[1,2,3],[7,1,1]]
    target = [7,2,3]
    print(sol.mergeTriplets(triplets, target)) # True
    triplets = [[2,5,6],[1,4,4],[5,7,5]]
    target = [5,4,6]
    print(sol.mergeTriplets(triplets, target)) # False