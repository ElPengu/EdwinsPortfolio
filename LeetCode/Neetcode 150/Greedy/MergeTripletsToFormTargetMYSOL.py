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

        - Let's think of this like a matrix
        - So each row is a triplet
        - And elements in the same column have the same index
        - Target = [x,y,z]
        - The only constraint is that we have to apply the operation 
        on EVERY element in a row at once!
        
        - We could arrange the triplets by the zeroth index
        - As soon as we see x in the zeroth index of triplets[i], 
        set res = triplets[i]
        - WHILE the zero...

        - No
        - Loop over triplets, and select all triplets whose index 0 
        holds exactly x 
        - Now...
        - Set res to be the first of these triplets
        - As you loop over the triplets, apply the operation only when 
        index 1 is equal to y
        - Finally, apply the operation only when index 2 is equal to 
        z AND y
        - Actually, no, this has some fail cases

        - Is it not possible to sort triplets by index 0, then index 1, 
        then index 2 in order of precedence
        - Then ...

        - WAIT
        - I THINK I GOT IT
        - Loop over triplets ...
        - Nope!

        - I feel like you would apply the operation when all elements 
        of the triplet are at most equal to the target elements 
        
        - YES, IT WORKS, MY INTUITION WORKS!
        - 20 MINUTES AND 20 SECONDS
        '''

        res = None
        x,y,z = target[0],target[1],target[2]
        for triplet in triplets:
            if triplet[0]<=x and triplet[1]<=y and triplet[2]<=z:
                if not res:
                    res = triplet
                else:
                    res = [max(res[0], triplet[0]),max(res[1], triplet[1]),max(res[2], triplet[2])]

        
        return res == target
        
        pass

if __name__ == "__main__":
    sol = Solution()
    triplets = [[1,2,3],[7,1,1]]
    target = [7,2,3]
    print(sol.mergeTriplets(triplets, target)) # True
    triplets = [[2,5,6],[1,4,4],[5,7,5]]
    target = [5,4,6]
    print(sol.mergeTriplets(triplets, target)) # False