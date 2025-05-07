from typing import List

class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        - n gas stations in circular array
        - gas[i] is gas you can get at station i
        - cost[i] is the amount of gas to travel from the ith station 
        to the (i+1)th station (the last is connected to the first)
        - You begin with an empty tank at a gas station
        - Which gas station can you start at to travel around in 1 circuit
        - At most 1 solution
        - If impossible, return -1

        - At station i, cost[i] tells you how much to reach the NEXT 
        station, and gas[i] tells you how much you can get
        
        - Let's reverse our thinking by assuming that we can FINISH at 
        the station we are at with no fuel left 
        - We are at station i
        - To have arrived at i, we would need to have been at i-1, and 
        then paid cost[i] fuel whilst refilling with gas[i] fuel
        - We now have x fuel left at station i-1
        - If we have x>=0 fuel then we could reach station i from i-1
        - What if we have x<0 fuel left?
        - Then we cannot start from station i-1. Maybe we could end 
        at station i-1
        - And so we repeat
        - If we ever reach station again that we failed at and fail 
        AGAIN, then it is impossible
        - Else, if you see a station that you have been at with >=0 
        fuel twice then return that station!
        - This motivates a failStations set, and a successStations set 
        '''


        # Trivial case - We start and finish at a station if there 
        # are no other stations
        if len(gas) == 1: return 0

        # We start with 0 fuel
        fuel = 0
        # We arbitrarily start at the 0th station
        station = 0

        # Check backwards from the last station
        for i in range(len(gas)-1,-1,-1):
            
            # We fueled up as much as possible to reach the 
            # next station
            fuel += gas[i]

            # We paid the cost in fuel
            fuel -= cost[i]

            # Did we have enough fuel at station i to reach i+1?
            if fuel >=0:
                # We did! Add this as a successful station

            pass

        # Return the station if it exists
        

if __name__ == "__main__":
    sol = Solution()
    gas = [1,2,3,4]
    cost = [2,2,4,1]
    print(sol.canCompleteCircuit(gas, cost)) # 3
    gas = [1,2,3]
    cost = [2,3,2]
    print(sol.canCompleteCircuit(gas, cost)) # -1